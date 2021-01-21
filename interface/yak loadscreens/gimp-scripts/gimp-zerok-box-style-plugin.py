#!/usr/bin/env python
# made by zenfur, 2018
# open source, BSD licence
# requires putting inside plugins directory for gimp, usually in ~/.gimp/plug-ins/, or /User/.gimp/plug-ins/ for windows.
# script will be available under Filters->Zero K->ZeroK Hint Box

from gimpfu import *
	
def	render_zerok_box(image, active_layer, hex_gauss_radius=70, bg_opacity=60.0, p=0.68, q=0.78):
	try:
		#image = gimp.image_list()[0]
		#active_layer = pdb.gimp_image_get_active_layer(image)
		x = active_layer.offsets[0]
		y = active_layer.offsets[1]
		width = active_layer.width
		height = active_layer.height

		def save_layer(layer, group):
			pdb.gimp_image_reorder_item(image, layer, group, -1)
			pdb.gimp_item_set_linked(layer, True)

		# layer group
		layer_group = pdb.gimp_layer_group_new(image)
		pdb.gimp_item_set_linked(layer_group, True)
		pdb.gimp_image_insert_layer(image, layer_group, None, 1)
		pdb.gimp_item_set_linked(layer_group, True)
			
		# background
		selection = pdb.gimp_image_select_round_rectangle(image, CHANNEL_OP_REPLACE, x, y, width, height, 10, 10)
		pdb.gimp_context_set_foreground("#000000")
		pdb.gimp_edit_bucket_fill(active_layer, FG_BUCKET_FILL, NORMAL_MODE, 100.0, 0, False, x, y)
		pdb.gimp_layer_set_opacity(active_layer, bg_opacity)
		save_layer(active_layer, layer_group)

		# hex pattern
		hex_layer = pdb.gimp_layer_new(image, width, height, RGBA_IMAGE, "hex_pattern", 100, NORMAL_MODE)#SOFTLIGHT_MODE)
		pdb.gimp_image_insert_layer(image, hex_layer, layer_group, -1)
		pdb.gimp_layer_set_offsets(hex_layer, x, y)
		pdb.gimp_context_set_foreground("#000000")
		pdb.gimp_edit_bucket_fill(hex_layer, BG_BUCKET_FILL, NORMAL_MODE, 100, 0, False, x, y)
		pdb.plug_in_mosaic(image, hex_layer, 17, 0, 1, 1.0, True, 90, 0.0, True, True, 1, 0, 0)
		pdb.gimp_image_select_item(image, CHANNEL_OP_REPLACE, hex_layer)
		pdb.gimp_edit_clear(hex_layer)
		pdb.gimp_selection_invert(image)
		pdb.gimp_edit_bucket_fill(hex_layer, BG_BUCKET_FILL, NORMAL_MODE, 100, 0, False, x, y)
		pdb.gimp_layer_set_opacity(hex_layer, 17.0)
		save_layer(hex_layer, layer_group)

		#adding mask to phase out hex
		mask = pdb.gimp_layer_create_mask(hex_layer, ADD_WHITE_MASK)
		pdb.gimp_layer_add_mask(hex_layer, mask)
		dx = width/2
		dy = height/2
		c_x = x + dx
		c_y = y + dy
		pdb.gimp_image_select_round_rectangle(image, CHANNEL_OP_REPLACE, c_x-dx*p, c_y-dy*p, width*p, height*p, 10, 10)
		pdb.gimp_image_select_ellipse(image, CHANNEL_OP_ADD, c_x-dx*q, c_y-dy*q, width*q, height*q)
		pdb.gimp_edit_bucket_fill(mask, FG_BUCKET_FILL, NORMAL_MODE, 100, 0, False, x, y)
		pdb.gimp_selection_none(image)
		pdb.plug_in_gauss(image, mask, hex_gauss_radius, hex_gauss_radius, 1)
		 

		# border
		border_layer = pdb.gimp_layer_new(image, width+4, height+4, RGBA_IMAGE, "border", 100, NORMAL_MODE)
		pdb.gimp_image_insert_layer(image, border_layer, layer_group, -1)
		pdb.gimp_layer_set_offsets(border_layer, x-2, y-2)
		selection = pdb.gimp_image_select_round_rectangle(image, CHANNEL_OP_REPLACE, x, y, width, height, 10, 10)
		pdb.gimp_selection_grow(image, 1)
		pdb.gimp_context_set_foreground("#37fff1")
		pdb.gimp_edit_bucket_fill(border_layer, FG_BUCKET_FILL, NORMAL_MODE, 100, 0, False, x, y)
		pdb.gimp_selection_shrink(image, 1)
		pdb.gimp_edit_clear(border_layer)
		pdb.gimp_selection_none(image)
		border_copy = pdb.gimp_layer_copy(border_layer, True)
		pdb.gimp_image_insert_layer(image, border_copy, layer_group, -1)
		pdb.plug_in_gauss(image, border_layer, 1, 1, 1)
		border_layer = pdb.gimp_image_merge_down(image, border_copy, EXPAND_AS_NECESSARY)
		pdb.gimp_item_set_linked(border_layer, True)
		save_layer(border_layer, layer_group)

		# border shadow
		pdb.script_fu_drop_shadow(image, border_layer, 1, 1, 3, "#000000", 90, True)
		save_layer(layer_group.layers[1], layer_group)

		# text box
		pdb.gimp_context_set_foreground("#FFFFFF")
		text_layer = pdb.gimp_text_layer_new(image, "     Start your description here...", "Arial Bold", 26, 0)
		pdb.gimp_image_insert_layer(image, text_layer, layer_group, -1)
		pdb.gimp_text_layer_resize(text_layer, int(width*0.9), int(height*0.9))
		pdb.gimp_layer_set_offsets(text_layer, x+0.05*width, y+0.05*height)
		pdb.gimp_context_set_foreground("#000000")
		save_layer(text_layer, layer_group)
	except Exception as err:
		gimp.message("Unexpected error: " + str(err))

	
register(
    "python_fu_gimp_zerok_box_style_plugin",
    "ZeroK Box Style plugin",
    "Draw a box with the same style as in advice loading screens.",
    "zenfur",
    "Open source",
    "2018",
    "<Image>/Filters/Zero K/ZeroK Hint Box",
    "*",
    [
	  (PF_INT, "hex_blur_radius", "How much hex grid mask is blurred", 70),
	  (PF_FLOAT, "bg_opacity", "Opacity of black background", 60.0),
	  (PF_SLIDER, "mask_rectangle_dimension", "How big area of rectangle in hex mask is", 0.7, (0.0, 1.0, 0.05)),
	  (PF_SLIDER, "mask_ellipse_dimension", "How big area of ellipse in hex mask is", 0.8, (0.0, 1.0, 0.05))
	],
    [],
    render_zerok_box)

main()
