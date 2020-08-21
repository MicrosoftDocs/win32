---
title: Direct3D 10 Frequently Asked Questions
description: This article contains some of the frequently asked questions surrounding Direct3D 10 from the point of view of a developer who is porting an existing application from Direct3D 9 (D3D9) to Direct3D 10 (D3D10).
ms.assetid: da3022ca-b120-d0d7-6747-65b946dbc73c
ms.topic: article
ms.date: 05/31/2018
---

# Direct3D 10 Frequently Asked Questions

This article contains some of the frequently asked questions surrounding Direct3D 10 from the point of view of a developer who is porting an existing application from Direct3D 9 (D3D9) to Direct3D 10 (D3D10).

-   [Constant Buffers](#constant-buffers)
-   [State](#state)
-   [Formats](#formats)
-   [Shader Linkage](#shader-linkage)
-   [Draw Calls](#draw-calls)
-   [Resources](#resources)
-   [Depth as Texture](#depth-as-texture)
-   [MSAA](#msaa)
-   [Crashes](#crashes)
-   [Predicated Rendering](#predicated-rendering)
-   [Geometry Shader](#geometry-shader)
-   [HLSL](#hlsl)

## Constant Buffers

<dl> <dt>

<span id="What_is_the_best_way_to_update_constant_buffers_"></span><span id="what_is_the_best_way_to_update_constant_buffers_"></span><span id="WHAT_IS_THE_BEST_WAY_TO_UPDATE_CONSTANT_BUFFERS_"></span>What is the best way to update constant buffers?
</dt> <dd>

UpdateSubresource and Map with Discard should be about the same speed. Choose between them depending on which one copies the least amount of memory. If you already have your data stored in memory in one contiguous block, use UpdateSubresource. If you need to accumulate data from other places, use Map with Discard.

</dd> <dt>

<span id="What_is_the_worst_way_to_organize_constant_buffers_"></span><span id="what_is_the_worst_way_to_organize_constant_buffers_"></span><span id="WHAT_IS_THE_WORST_WAY_TO_ORGANIZE_CONSTANT_BUFFERS_"></span>What is the worst way to organize constant buffers?
</dt> <dd>

The worst performance is realized by putting all constants for a particular shader into one constant buffer. While this often is the easiest way to port from D3D9 to D3D10, it can cripple performance. For example, consider a scenario that uses the following constant buffer:

``` syntax
cbuffer VSGlobalsCB
{
    matrix  ViewProj;
    matrix  Bones[100];
    matrix  World;
    float   SpecPower;
    float4  BDRFCoefficients;
    float   AppTime;
    uint2   RenderTargetSize;
};
```

The buffer is 6560 bytes. Assume there is an application with 1000 objects to be rendered, 100 of which are skinned meshes, and 900 of which are static meshes. Also, assume that this application is using shadow mapping with one light source. This means there are two passes, one for the depth map rendered from the light, and one for the forward rendering pass. This results in 2000 draw calls. Although each draw call does not NEED to update every part of the constant buffer, the entire constant buffer still is updated and sent to the card. This results in the update of 13 MB of data every frame (2000 draw calls times 6560 KB).

</dd> <dt>

<span id="What_is_the_best_way_to_organize_my_constant_buffers_"></span><span id="what_is_the_best_way_to_organize_my_constant_buffers_"></span><span id="WHAT_IS_THE_BEST_WAY_TO_ORGANIZE_MY_CONSTANT_BUFFERS_"></span>What is the best way to organize my constant buffers?
</dt> <dd>

The best way is to organize constant buffers by frequency of update. Constants that are updated at similar frequencies should be in the same buffer. For example, consider the scenario presented under, "What is the worst way to organize constant buffers?," but with a better constant layout:

``` syntax
cbuffer VSGlobalPerFrameCB
  { 
    float   AppTime; 
  };
cbuffer VSPerSkinnedCB
  { 
    matrix  Bones[100]; 
  };
cbuffer VSPerStaticCB
  {
    matrix  World;
  };
cbuffer VSPerPassCB
  {
    matrix  ViewProj;
    uint2   RenderTargetSize;
  };
cbuffer VSPerMaterialCB
  {
    float   SpecPower;
    float4  BDRFCoefficients;
  };    
```

Constant buffers are split by their update frequency, but this only is half of the solution. The application needs to update the constant buffers correctly in order to take full advantage of the split. We will assume the same scene as above: 900 static meshes, 100 skinned meshes, one light pass, and one forward pass. We also will assume that some constant buffers per-object will be stored. This means that each object will contain either a VSPerSkinnedCB or a VSPerStaticCB, depending on whether or not it is skinned or static. We do this in order to avoid doubling the amount of matrices sent through the pipeline.

We split the frame into three phases. The first phase is the beginning of the frame and involves no rendering, just constant updates.

<dl> <dt>

<span id="Begin_Frame"></span><span id="begin_frame"></span><span id="BEGIN_FRAME"></span>**Begin Frame**
</dt> <dd>

-   Update VSGlobalPerFrameCB for application time (4 bytes)
-   Update 100 VSPerSkinnedCB for the 100 skinned objects (640000 bytes)
-   Update VSPerStaticCB for 900 static objects (57600 bytes)

Next is the shadow map pass. Notice that the only constant buffer that actually updates is VSPerPassCB. All other constant buffers were updated during the begin frame pass. While we still need to bind these constant buffers, the amount of information passed to the video card is minimal, because the buffers already have been updated.

</dd> <dt>

<span id="Shadow_Pass"></span><span id="shadow_pass"></span><span id="SHADOW_PASS"></span>**Shadow Pass**
</dt> <dd>

-   Update VSPerPassCB (72 bytes)
-   Draw 100 skinned meshes (100 binds, no updates)
-   Draw 900 static meshes (100 binds, no updates)

Similarly, the forward rendering pass only needs to update per-material data, because it was not stored per-mesh. If we assume that there are 500 materials in use in the scene:

</dd> <dt>

<span id="Forward_Pass"></span><span id="forward_pass"></span><span id="FORWARD_PASS"></span>**Forward Pass**
</dt> <dd>

-   Update VSPerPassCB (72 bytes)
-   Update 500 VSPerMaterialCBs (10000 bytes)

This results in a total of just 707 KB. Although this is a very contrived scenario, it illustrates just how much constant update overhead can be reduced by sorting constants by frequency of update.

</dd> </dl> </dd> <dt>

<span id="What_if_I_do_not_have_enough_space_to_store_individual_constant_buffers_for_my_meshes__material__and_so_on___"></span><span id="what_if_i_do_not_have_enough_space_to_store_individual_constant_buffers_for_my_meshes__material__and_so_on___"></span><span id="WHAT_IF_I_DO_NOT_HAVE_ENOUGH_SPACE_TO_STORE_INDIVIDUAL_CONSTANT_BUFFERS_FOR_MY_MESHES__MATERIAL__AND_SO_ON___"></span>What if I do not have enough space to store individual constant buffers for my meshes, material, and so on? 
</dt> <dd>

You always can use a tiered system of constant buffers. Create variable-sized constant buffers (16 bytes, 32 bytes, 64 bytes, and so on) up to the largest constant buffer size needed. When it is time to bind a constant buffer to a shader, select the smallest constant buffer that can hold the data needed by the shader. Although this approach is slightly less efficient, it is a good intermediate step.

</dd> <dt>

<span id="I_am_sharing_constant_buffers_between_different_shaders._One_shader_may_use_all_of_the_constants__but_another_may_use_some_of_the_constants._What_is_the_best_way_to_update_these___"></span><span id="i_am_sharing_constant_buffers_between_different_shaders._one_shader_may_use_all_of_the_constants__but_another_may_use_some_of_the_constants._what_is_the_best_way_to_update_these___"></span><span id="I_AM_SHARING_CONSTANT_BUFFERS_BETWEEN_DIFFERENT_SHADERS._ONE_SHADER_MAY_USE_ALL_OF_THE_CONSTANTS__BUT_ANOTHER_MAY_USE_SOME_OF_THE_CONSTANTS._WHAT_IS_THE_BEST_WAY_TO_UPDATE_THESE___"></span>I am sharing constant buffers between different shaders. One shader may use all of the constants, but another may use some of the constants. What is the best way to update these? 
</dt> <dd>

One approach is to split the constant buffer even further. However, there comes a point at which too many constant buffers are bound. In this case, move the constants that are likely to be unused by several shaders to the end of the constant buffer. When getting the variable data from the shader, use the D3D10\_SVF\_USED flag from the D3D10\_SHADER\_VARIABLE\_DESC to determine if the variable is used. By placing unused variables at the end of the constant buffer, you can bind a smaller buffer to the shader that does not use these variables, thus saving the update cost.

</dd> <dt>

<span id="How_much_can_I_improve_my_frame_rate_if_I_only_upload_my_character_s_bones_once_per_frame_instead_of_once_per_pass_draw___"></span><span id="how_much_can_i_improve_my_frame_rate_if_i_only_upload_my_character_s_bones_once_per_frame_instead_of_once_per_pass_draw___"></span><span id="HOW_MUCH_CAN_I_IMPROVE_MY_FRAME_RATE_IF_I_ONLY_UPLOAD_MY_CHARACTER_S_BONES_ONCE_PER_FRAME_INSTEAD_OF_ONCE_PER_PASS_DRAW___"></span>How much can I improve my frame rate if I only upload my character's bones once per frame instead of once per pass/draw? 
</dt> <dd>

You can improve frame rate between 8 percent and 50 percent depending on the amount of redundant data. In the worst case, performance will not be reduced.

</dd> <dt>

<span id="How_many_constant_buffers_should_I_have_bound_at_once__"></span><span id="how_many_constant_buffers_should_i_have_bound_at_once__"></span><span id="HOW_MANY_CONSTANT_BUFFERS_SHOULD_I_HAVE_BOUND_AT_ONCE__"></span>How many constant buffers should I have bound at once? 
</dt> <dd>

Bind the minimum number of constant buffers it takes to get all of your data into the shader. In a realistic scenario, five is the recommended number of constant buffers to use. Sharing constant buffers between shaders (binding the same CB to the VS and PS) also can improve performance.

</dd> <dt>

<span id="Is_there_a_cost_for_binding_constant_buffers_without_using_them__"></span><span id="is_there_a_cost_for_binding_constant_buffers_without_using_them__"></span><span id="IS_THERE_A_COST_FOR_BINDING_CONSTANT_BUFFERS_WITHOUT_USING_THEM__"></span>Is there a cost for binding constant buffers without using them? 
</dt> <dd>

Yes, if you are not actually going to use the buffer, then do not call VSSetConsantBuffer or PSSetConstantBuffer. This extra API overhead can add up over the course of multiple draw calls.

</dd> </dl>

## State

<dl> <dt>

<span id="What_is_the_best_way_to_manage_state_in_D3D10___"></span><span id="what_is_the_best_way_to_manage_state_in_d3d10___"></span><span id="WHAT_IS_THE_BEST_WAY_TO_MANAGE_STATE_IN_D3D10___"></span>What is the best way to manage state in D3D10? 
</dt> <dd>

The best solution is to know all of your state up front and to create the state objects up front. This means that at render time, state binding is the only operation that needs to happen. D3D10 also filter outs duplicates.

</dd> <dt>

<span id="My_game_has_dynamically_loaded_or_has_user-generated_content._I_cannot_load_all_of_my_state_objects_up_front._What_should_I_do___"></span><span id="my_game_has_dynamically_loaded_or_has_user-generated_content._i_cannot_load_all_of_my_state_objects_up_front._what_should_i_do___"></span><span id="MY_GAME_HAS_DYNAMICALLY_LOADED_OR_HAS_USER-GENERATED_CONTENT._I_CANNOT_LOAD_ALL_OF_MY_STATE_OBJECTS_UP_FRONT._WHAT_SHOULD_I_DO___"></span>My game has dynamically loaded or has user-generated content. I cannot load all of my state objects up front. What should I do? 
</dt> <dd>

There are two solutions here. The first is to just create state objects on the fly and to let D3D10 filter out duplicates. This, however, is not recommended for scenarios with many state object changes per frame. A better solution is to hash the state objects yourself and to create a state object only if one that fits the requirements is not found in the hash table. The reasoning behind using a custom hash table is that an application can select a fast hash based upon the usage scenario particular to that application. For example, if an application only changes the rendertargetwritemask in the BlendState and keeps all other values the same, the application can generate a hash from the rendertargetwritemask instead of the entire structure.

</dd> <dt>

<span id="AlphaTest_state_is_gone._Where_did_it_go___"></span><span id="alphatest_state_is_gone._where_did_it_go___"></span><span id="ALPHATEST_STATE_IS_GONE._WHERE_DID_IT_GO___"></span>AlphaTest state is gone. Where did it go? 
</dt> <dd>

AlphaTest now should be performance in the shader. See the FixedFuncEMU sample.

</dd> <dt>

<span id="What_happened_to_user_clip_planes___"></span><span id="what_happened_to_user_clip_planes___"></span><span id="WHAT_HAPPENED_TO_USER_CLIP_PLANES___"></span>What happened to user clip planes? 
</dt> <dd>

User clip planes have moved into the shader. There are two ways to handle this. The first is to output SV\_ClipDistance from the vertex shader or the geometry shader. The other option is to use discard in the pixel shader based upon some value passed down by the vertex shader or the geometry shader. Experiment with both to see which is faster for your particular scenario. Using SV\_ClipDistance could cause the hardware to use a geometry-based clipping routine that may cause geometry bound draw calls to run slower. Likewise, using discard shifts the work to the pixel shader, which may cause pixel-bound draw calls to run slower.

</dd> <dt>

<span id="Clears_do_not_respect_any_state_settings__such_as_my_scissor_rect_settings_in_my_Rasterizer_State.__"></span><span id="clears_do_not_respect_any_state_settings__such_as_my_scissor_rect_settings_in_my_rasterizer_state.__"></span><span id="CLEARS_DO_NOT_RESPECT_ANY_STATE_SETTINGS__SUCH_AS_MY_SCISSOR_RECT_SETTINGS_IN_MY_RASTERIZER_STATE.__"></span>Clears do not respect any state settings, such as my scissor rect settings in my Rasterizer State. 
</dt> <dd>

Clears have been separated from the pipeline state. In order to get D3D9-style behavior, emulate clears by drawing a full-screen quad.

</dd> <dt>

<span id="I_set_my_states_back_to_default_to_try_and_diagnose_a_rendering_error._Now_my_screen_just_shows_black__although_I_know_I_am_drawing_objects_onto_the_screen.__"></span><span id="i_set_my_states_back_to_default_to_try_and_diagnose_a_rendering_error._now_my_screen_just_shows_black__although_i_know_i_am_drawing_objects_onto_the_screen.__"></span><span id="I_SET_MY_STATES_BACK_TO_DEFAULT_TO_TRY_AND_DIAGNOSE_A_RENDERING_ERROR._NOW_MY_SCREEN_JUST_SHOWS_BLACK__ALTHOUGH_I_KNOW_I_AM_DRAWING_OBJECTS_ONTO_THE_SCREEN.__"></span>I set my states back to default to try and diagnose a rendering error. Now my screen just shows black, although I know I am drawing objects onto the screen. 
</dt> <dd>

When setting state back to default values (NULL), ensure that the SampleMask in the call to OMSetBlendState is never zero. If SampleMask is set to zero, then all samples will logically AND with zero. In this scenario, no samples will pass the blend test.

</dd> <dt>

<span id="Where_did_the_D3DSAMP_SRGBTEXTURE_state_go___"></span><span id="where_did_the_d3dsamp_srgbtexture_state_go___"></span><span id="WHERE_DID_THE_D3DSAMP_SRGBTEXTURE_STATE_GO___"></span>Where did the D3DSAMP\_SRGBTEXTURE state go? 
</dt> <dd>

SRGB was removed as part of the sampler state and now is tied to the texture format. Binding an SRGB texture will result in the same sampling you would get if you specified D3DSAMP\_SRGBTEXTURE in Direct3D 9.

</dd> </dl>

## Formats

<dl> <dt>

<span id="Which_D3D9_format_corresponds_to_which_D3D10_format___"></span><span id="which_d3d9_format_corresponds_to_which_d3d10_format___"></span><span id="WHICH_D3D9_FORMAT_CORRESPONDS_TO_WHICH_D3D10_FORMAT___"></span>Which D3D9 format corresponds to which D3D10 format? 
</dt> <dd>

For info, see [Direct3D 9 to Direct3D 10 Considerations](/windows/desktop/direct3d10/d3d10-graphics-programming-guide-d3d9-to-d3d10-considerations).

</dd> <dt>

<span id="What_happened_to_A8R8G8B8_texture_formats___"></span><span id="what_happened_to_a8r8g8b8_texture_formats___"></span><span id="WHAT_HAPPENED_TO_A8R8G8B8_TEXTURE_FORMATS___"></span>What happened to A8R8G8B8 texture formats? 
</dt> <dd>

They have been deprecated in D3D10. You can re-source your textures as R8G8B8A8, or you can swizzle on load, or you can swizzle in the shader.

</dd> <dt>

<span id="How_do_I_use_palettized_textures___"></span><span id="how_do_i_use_palettized_textures___"></span><span id="HOW_DO_I_USE_PALETTIZED_TEXTURES___"></span>How do I use palettized textures? 
</dt> <dd>

Place your color palette in a texture or a constant buffer and bind it to the pipeline. In the pixel shader do an indirect lookup using the index in your palettized texture.

</dd> <dt>

<span id="What_are_these_new_SRGB_formats___"></span><span id="what_are_these_new_srgb_formats___"></span><span id="WHAT_ARE_THESE_NEW_SRGB_FORMATS___"></span>What are these new SRGB formats? 
</dt> <dd>

SRGB was removed as part of the sampler state and is now tied to the texture format. Binding an SRGB texture will result in the same sampling you would get if you specified D3DSAMP\_SRGBTEXTURE in Direct3D 9.

</dd> <dt>

<span id="Where_did_triangle_fans_go___"></span><span id="where_did_triangle_fans_go___"></span><span id="WHERE_DID_TRIANGLE_FANS_GO___"></span>Where did triangle fans go? 
</dt> <dd>

Triangle fans have been deprecated in D3D10. Triangle fans will need to be converted either in the content pipeline or on load.

</dd> </dl>

## Shader Linkage

<dl> <dt>

<span id="My_Direct3D_9_shaders_compile_fine_to_Shader_Model_4.0__but_when_I_bind_them_to_the_pipeline__I_get_linkage_errors_showing_up_in_the_debug_output_with_the_debug_runtime.__"></span><span id="my_direct3d_9_shaders_compile_fine_to_shader_model_4.0__but_when_i_bind_them_to_the_pipeline__i_get_linkage_errors_showing_up_in_the_debug_output_with_the_debug_runtime.__"></span><span id="MY_DIRECT3D_9_SHADERS_COMPILE_FINE_TO_SHADER_MODEL_4.0__BUT_WHEN_I_BIND_THEM_TO_THE_PIPELINE__I_GET_LINKAGE_ERRORS_SHOWING_UP_IN_THE_DEBUG_OUTPUT_WITH_THE_DEBUG_RUNTIME.__"></span>My Direct3D 9 shaders compile fine to Shader Model 4.0, but when I bind them to the pipeline, I get linkage errors showing up in the debug output with the debug runtime. 
</dt> <dd>

Shader linkage is much stricter in D3D10. Elements in a subsequent stage must be read in the order they are output from the previous stage. For example:

A vertex shader outputs:

``` syntax
    float4 Pos  : SV_POSITION;
    float3 Norm : NORMAL;
    float2 Tex  : TEXCOORD0;
```

A pixel shader reads in:

``` syntax
        float3 Norm : NORMAL;
        float2 Tex  : TEXCOORD0;
```

Although the position is not needed in the pixel shader, this will cause a linkage error, because position is being output from the vertex shader, but not read by the pixel shader. The more correct version would look like this:

A vertex shader outputs:

``` syntax
        float3 Norm : NORMAL;
        float2 Tex  : TEXCOORD0;
        float4 Pos  : SV_POSITION;
```

A pixel shader reads in:

``` syntax
        float3 Norm : NORMAL;
        float2 Tex  : TEXCOORD0;
```

In this case, the vertex shader is outputting the same information, but now the pixel shader is reading things in the order output. Because the pixel shader is not reading anything after Tex, we do not have to worry that the VS is outputting more information than the PS is reading.

</dd> <dt>

<span id="I_need_a_shader_signature_in_order_to_create_an_Input_Layout__but_I_load_my_meshes_and_create_layouts_before_creating_shaders._What_do_I_do___"></span><span id="i_need_a_shader_signature_in_order_to_create_an_input_layout__but_i_load_my_meshes_and_create_layouts_before_creating_shaders._what_do_i_do___"></span><span id="I_NEED_A_SHADER_SIGNATURE_IN_ORDER_TO_CREATE_AN_INPUT_LAYOUT__BUT_I_LOAD_MY_MESHES_AND_CREATE_LAYOUTS_BEFORE_CREATING_SHADERS._WHAT_DO_I_DO___"></span>I need a shader signature in order to create an Input Layout, but I load my meshes and create layouts before creating shaders. What do I do? 
</dt> <dd>

One solution is to switch the order and load shaders before loading meshes. However, this is much easier said than done. You always can create the Input Layouts on demand when needed by the application. You will have to keep a version of the shader signature around. You should create a hash based off of the shader and buffer layout, and only create the Input Layout if one that matches does not exist already.

</dd> </dl>

## Draw Calls

<dl> <dt>

<span id="What_is_my_limit_on_draw_calls_for_D3D10_to_reach_60_Hz__30_Hz___"></span><span id="what_is_my_limit_on_draw_calls_for_d3d10_to_reach_60_hz__30_hz___"></span><span id="WHAT_IS_MY_LIMIT_ON_DRAW_CALLS_FOR_D3D10_TO_REACH_60_HZ__30_HZ___"></span>What is my limit on draw calls for D3D10 to reach 60 Hz? 30 Hz? 
</dt> <dd>

Direct3D 9 had a limitation on the number of draw calls because of the CPU cost per draw call. On Direct3D 10, the cost of each draw call has been reduced. However, there is no longer a definite correlation between draw calls and frame rates. Because draw calls often require many support calls ( constant buffer updates, texture bindings, state setting, and so on) the frame rate impact of the API is now more dependent on the overall API usage as opposed to simply draw call counts.

</dd> </dl>

## Resources

<dl> <dt>

<span id="What_resource_usage_type_should_I_use_for_what_operations___"></span><span id="what_resource_usage_type_should_i_use_for_what_operations___"></span><span id="WHAT_RESOURCE_USAGE_TYPE_SHOULD_I_USE_FOR_WHAT_OPERATIONS___"></span>What resource usage type should I use for what operations? 
</dt> <dd>

Use the following cheat-sheet:

-   The CPU updates the resource more than once per frame: D3D10\_USAGE\_DYNAMIC
-   The CPU updates the resource less than once per frame: D3D10\_USAGE\_DEFAULT
-   The CPU does not update the resource: D3D10\_USAGE\_IMMUTABLE
-   The CPU needs to read the resource: D3D10\_USAGE\_STAGING

Because constant buffers are always meant to be update frequently, they do not conform to the "cheat-sheet." For which resource types to use for constant buffers, see the [Constant Buffers](#constant-buffers) section.

</dd> <dt>

<span id="What_happened_to_DrawPrimitiveUP_and_DrawIndexedPrimitiveUP___"></span><span id="what_happened_to_drawprimitiveup_and_drawindexedprimitiveup___"></span><span id="WHAT_HAPPENED_TO_DRAWPRIMITIVEUP_AND_DRAWINDEXEDPRIMITIVEUP___"></span>What happened to DrawPrimitiveUP and DrawIndexedPrimitiveUP? 
</dt> <dd>

They are gone in D3D10. For dynamic geometry use a large D3D10\_USAGE\_DYNAMIC buffer. At the beginning of the frame, map it with D3D10\_MAP\_WRITE\_DISCARD. For each subsequent draw call advance the write pointer past the position of the previously drawn vertices and map the buffer with D3D10\_MAP\_WRITE\_NO\_OVERWRITE. If you near the end of the buffer before the end of the frame, wrap the write pointer around to the beginning and map with D3D10\_MAP\_WRITE\_DISCARD.

</dd> <dt>

<span id="Can_I_write_16-bit_indices_and_32-bit_indices_into_the_same_dynamic_geometry_buffer___"></span><span id="can_i_write_16-bit_indices_and_32-bit_indices_into_the_same_dynamic_geometry_buffer___"></span><span id="CAN_I_WRITE_16-BIT_INDICES_AND_32-BIT_INDICES_INTO_THE_SAME_DYNAMIC_GEOMETRY_BUFFER___"></span>Can I write 16-bit indices and 32-bit indices into the same dynamic geometry buffer? 
</dt> <dd>

Yes, you can, but this can incur a performance penalty on certain hardware. It is a safer to create separate buffers for dynamic 16-bit index data and 32-bit index data.

</dd> <dt>

<span id="How_do_I_read_data_back_from_the_GPU_to_the_CPU___"></span><span id="how_do_i_read_data_back_from_the_gpu_to_the_cpu___"></span><span id="HOW_DO_I_READ_DATA_BACK_FROM_THE_GPU_TO_THE_CPU___"></span>How do I read data back from the GPU to the CPU? 
</dt> <dd>

You must use a staging resource. Copy the data from the GPU resource to the staging resource using CopyResource. Map the staging resource to read the data.

</dd> <dt>

<span id="My_application_was_dependent_on_StretchRect_functionality.__"></span><span id="my_application_was_dependent_on_stretchrect_functionality.__"></span><span id="MY_APPLICATION_WAS_DEPENDENT_ON_STRETCHRECT_FUNCTIONALITY.__"></span>My application was dependent on StretchRect functionality. 
</dt> <dd>

Because this was essentially a wrapper for basic Direct3D functionality, it was removed from the API. Some of the StretchRect functionality was moved into D3DX10LoadTextureFromTexture. For format conversions and copying textures, D3DX10LoadTextureFromTexture may do the job. However, operations such as converting from one size to another likely will require a render to texture operation in the application.

</dd> <dt>

<span id="There_are_no_offsets_or_sizes_on_Map_calls_for_resources._These_were_there_on_Lock_calls_on_Direct3D_9__why_did_they_change___"></span><span id="there_are_no_offsets_or_sizes_on_map_calls_for_resources._these_were_there_on_lock_calls_on_direct3d_9__why_did_they_change___"></span><span id="THERE_ARE_NO_OFFSETS_OR_SIZES_ON_MAP_CALLS_FOR_RESOURCES._THESE_WERE_THERE_ON_LOCK_CALLS_ON_DIRECT3D_9__WHY_DID_THEY_CHANGE___"></span>There are no offsets or sizes on Map calls for resources. These were there on Lock calls on Direct3D 9; why did they change? 
</dt> <dd>

The offsets and sizes on Lock calls on Direct3D 9 were basically API clutter and often ignored by the driver. Offsets should be calculated instead by the application from the pointer returned in the Map call.

</dd> </dl>

## Depth as Texture

<dl> <dt>

<span id="Which_is_faster__Using_depth_as_a_texture_or_writing_depth_to_alpha_and_reading_that___"></span><span id="which_is_faster__using_depth_as_a_texture_or_writing_depth_to_alpha_and_reading_that___"></span><span id="WHICH_IS_FASTER__USING_DEPTH_AS_A_TEXTURE_OR_WRITING_DEPTH_TO_ALPHA_AND_READING_THAT___"></span>Which is faster? Using depth as a texture or writing depth to alpha and reading that? 
</dt> <dd>

This is application and hardware specific. Use whichever one saves the most bandwidth. If you already are using multiple render targets and have an extra channel, then writing depth from the shader may be a better solution. Also, writing depth to alpha or another render target allows you to write linear depth values that may speed up calculations that need to access the depth buffer.

</dd> <dt>

<span id="Can_I_have_a_texture_bound_as_an_input_AND_bound_as_a_depth-stencil_texture_as_long_as_I_disable_depth_writes___"></span><span id="can_i_have_a_texture_bound_as_an_input_and_bound_as_a_depth-stencil_texture_as_long_as_i_disable_depth_writes___"></span><span id="CAN_I_HAVE_A_TEXTURE_BOUND_AS_AN_INPUT_AND_BOUND_AS_A_DEPTH-STENCIL_TEXTURE_AS_LONG_AS_I_DISABLE_DEPTH_WRITES___"></span>Can I have a texture bound as an input AND bound as a depth-stencil texture as long as I disable depth writes? 
</dt> <dd>

Not in D3D10.

</dd> </dl>

## MSAA

<dl> <dt>

<span id="Can_I_resolve_an_MSAA_depth-stencil_texture___"></span><span id="can_i_resolve_an_msaa_depth-stencil_texture___"></span><span id="CAN_I_RESOLVE_AN_MSAA_DEPTH-STENCIL_TEXTURE___"></span>Can I resolve an MSAA depth-stencil texture? 
</dt> <dd>

Not in D3D10. However, you can sample individual samples from the MSAA texture. See the [HLSL](#hlsl) section for details.

</dd> <dt>

<span id="Why_does_my_application_crash_as_soon_as_I_enable_MSAA___"></span><span id="why_does_my_application_crash_as_soon_as_i_enable_msaa___"></span><span id="WHY_DOES_MY_APPLICATION_CRASH_AS_SOON_AS_I_ENABLE_MSAA___"></span>Why does my application crash as soon as I enable MSAA? 
</dt> <dd>

Ensure you are enabling an MSAA sample count and quality number that actually are enumerated by the driver.

</dd> </dl>

## Crashes

<dl> <dt>

<span id="My_application_crashes_in_D3D10_or_in_the_driver_and_I_do_not_know_why.__"></span><span id="my_application_crashes_in_d3d10_or_in_the_driver_and_i_do_not_know_why.__"></span><span id="MY_APPLICATION_CRASHES_IN_D3D10_OR_IN_THE_DRIVER_AND_I_DO_NOT_KNOW_WHY.__"></span>My application crashes in D3D10 or in the driver and I do not know why. 
</dt> <dd>

The first step is to enable the debug runtime ([**D3D10\_CREATE\_DEVICE\_DEBUG**](/windows/desktop/api/d3d10/ne-d3d10-d3d10_create_device_flag) flag passed into [**D3D10CreateDevice**](/windows/desktop/api/d3d10misc/nf-d3d10misc-d3d10createdevice)). This will expose the most common errors as debug output.

</dd> <dt>

<span id="PIX_crashes_when_I_try_to_use_my_application_with_it.__"></span><span id="pix_crashes_when_i_try_to_use_my_application_with_it.__"></span><span id="PIX_CRASHES_WHEN_I_TRY_TO_USE_MY_APPLICATION_WITH_IT.__"></span>PIX crashes when I try to use my application with it. 
</dt> <dd>

The first step is to enable the debug runtime ([**D3D10\_CREATE\_DEVICE\_DEBUG**](/windows/desktop/api/d3d10/ne-d3d10-d3d10_create_device_flag) flag passed into [**D3D10CreateDevice**](/windows/desktop/api/d3d10misc/nf-d3d10misc-d3d10createdevice)). PIX has a much higher probability of crashing if the debug output is not clean.

</dd> <dt>

<span id="My_game_runs_out_of_virtual_address_space_on_32-bit_Vista_under_D3D10._It_does_not_have_problems_on_D3D9.__"></span><span id="my_game_runs_out_of_virtual_address_space_on_32-bit_vista_under_d3d10._it_does_not_have_problems_on_d3d9.__"></span><span id="MY_GAME_RUNS_OUT_OF_VIRTUAL_ADDRESS_SPACE_ON_32-BIT_VISTA_UNDER_D3D10._IT_DOES_NOT_HAVE_PROBLEMS_ON_D3D9.__"></span>My game runs out of virtual address space on 32-bit Vista under D3D10. It does not have problems on D3D9. 
</dt> <dd>

There were some issues with D3D10 and virtual address space. This has been fixed in [KB940105](https://support.microsoft.com/kb/940105). If that does not fix your problem, ensure you are not creating more resources that can be mapped (locked) in D3D10 than you were creating in D3D9. Also think about porting to 64-bit since this will become more prevalent in the future.

</dd> </dl>

## Predicated Rendering

<dl> <dt>

<span id="I_used_Predicated_rendering__based_on_occlusion_query_results_._Why_is_my_app_still_the_same_speed___"></span><span id="i_used_predicated_rendering__based_on_occlusion_query_results_._why_is_my_app_still_the_same_speed___"></span><span id="I_USED_PREDICATED_RENDERING__BASED_ON_OCCLUSION_QUERY_RESULTS_._WHY_IS_MY_APP_STILL_THE_SAME_SPEED___"></span>I used Predicated rendering (based on occlusion query results). Why is my app still the same speed? 
</dt> <dd>

First, ensure that the rendering you would like to skip is actually the application bottleneck. If it is not the bottleneck, then skipping the rendering will not help frame rate.

Second, make sure that enough time has passed between the issue of the query and rendering that you wish to predicate. If the query has not finished by the time the render call hits the GPU, the rendering will occur anyway.

Third, predication only skips certain calls. The calls that are skipped are Draw, Clear, Copy, Update, ResolveSubresource and GenerateMips. State setting, IA setup, Map, and Create calls do not respect predication. If there are a lot of state setting calls around the draw call to be predicated, these states still will be set.

</dd> </dl>

## Geometry Shader

<dl> <dt>

<span id="Should_I_use_the_geometry_shader_to_tessellate_my__insert_anything_here____"></span><span id="should_i_use_the_geometry_shader_to_tessellate_my__insert_anything_here____"></span><span id="SHOULD_I_USE_THE_GEOMETRY_SHADER_TO_TESSELLATE_MY__INSERT_ANYTHING_HERE____"></span>Should I use the geometry shader to tessellate my (insert anything here)? 
</dt> <dd>

No. The geometry shader should NOT be used for tessellation.

</dd> <dt>

<span id="Can_I_use_the_geometry_shader_to_create_geometry___"></span><span id="can_i_use_the_geometry_shader_to_create_geometry___"></span><span id="CAN_I_USE_THE_GEOMETRY_SHADER_TO_CREATE_GEOMETRY___"></span>Can I use the geometry shader to create geometry? 
</dt> <dd>

Yes, in very limited scenarios. The geometry shader in current D3D10 (2008) parts is not equipped to handle much expansion. This may change in the future. Video card vendors may have a special path for one to four expansions because of existing point-sprite hardware. Any other expansion would have to be very limited. The ParticlesGS and PipesGS samples achieve high frame rates by only doing limited expansion. Only a few points are expanded per frame.

</dd> <dt>

<span id="What_should_I_use_the_geometry_shader_for___"></span><span id="what_should_i_use_the_geometry_shader_for___"></span><span id="WHAT_SHOULD_I_USE_THE_GEOMETRY_SHADER_FOR___"></span>What should I use the geometry shader for? 
</dt> <dd>

Anything that requires operations on an entire primitive such as silhouette detection, barycentric coordinates, and so on. Also use it to select which slice of a render target array to send primitives to.

</dd> <dt>

<span id="Can_I_output_variable_amounts_of_geometry_from_the_geometry_shader___"></span><span id="can_i_output_variable_amounts_of_geometry_from_the_geometry_shader___"></span><span id="CAN_I_OUTPUT_VARIABLE_AMOUNTS_OF_GEOMETRY_FROM_THE_GEOMETRY_SHADER___"></span>Can I output variable amounts of geometry from the geometry shader? 
</dt> <dd>

Yes, but this can cause performance issues. Take the example of outputting 1 point for one invocation and 4 points for another. While fitting within the expansion guidelines, this can cause the geometry shader threads to run serially.

</dd> <dt>

<span id="How_does_D3D10_know_how_to_generate_adjacency_indices_for_my_mesh__Or__why_does_D3D10_not_render_correctly_when_I_specify_that_the_geometry_shader_needs_adjacency_information.__"></span><span id="how_does_d3d10_know_how_to_generate_adjacency_indices_for_my_mesh__or__why_does_d3d10_not_render_correctly_when_i_specify_that_the_geometry_shader_needs_adjacency_information.__"></span><span id="HOW_DOES_D3D10_KNOW_HOW_TO_GENERATE_ADJACENCY_INDICES_FOR_MY_MESH__OR__WHY_DOES_D3D10_NOT_RENDER_CORRECTLY_WHEN_I_SPECIFY_THAT_THE_GEOMETRY_SHADER_NEEDS_ADJACENCY_INFORMATION.__"></span>How does D3D10 know how to generate adjacency indices for my mesh? Or, why does D3D10 not render correctly when I specify that the geometry shader needs adjacency information. 
</dt> <dd>

The adjacency information is not created by D3D10, but by the application. Adjacency indices are generated by the application and must contain six indices per primitive; of the six, the odd numbered indices are the edge adjacent vertices. ID3DX10Mesh::GenerateAdjacencyAndPointsReps can be used to generate this data.

</dd> </dl>

## HLSL

<dl> <dt>

<span id="Are_integer_and_bitwise_instructions_slow___"></span><span id="are_integer_and_bitwise_instructions_slow___"></span><span id="ARE_INTEGER_AND_BITWISE_INSTRUCTIONS_SLOW___"></span>Are integer and bitwise instructions slow? 
</dt> <dd>

They can be. Various D3D10 cards may be able only to issue integer operations on a subset of the available ALU units. This is highly dependent on the hardware. See your individual hardware vendor for recommendations on how to address integer operations on that particular hardware. Also, be very careful of casts between types.

</dd> <dt>

<span id="What_happened_to_VPOS___"></span><span id="what_happened_to_vpos___"></span><span id="WHAT_HAPPENED_TO_VPOS___"></span>What happened to VPOS? 
</dt> <dd>

If you declare an input to your pixel shader as SV\_POSITION, you will get the same behavior as declaring it as VPOS.

</dd> <dt>

<span id="How_do_I_sample_an_MSAA_texture___"></span><span id="how_do_i_sample_an_msaa_texture___"></span><span id="HOW_DO_I_SAMPLE_AN_MSAA_TEXTURE___"></span>How do I sample an MSAA texture? 
</dt> <dd>

In your shader, declare your texture as Texture2DMS. You then can fetch individual samples using the Sample methods off of the Texture2DMS object.

</dd> <dt>

<span id="How_do_I_tell_if_a_shader_variable_in_a_constant_buffer_actually_is_used___"></span><span id="how_do_i_tell_if_a_shader_variable_in_a_constant_buffer_actually_is_used___"></span><span id="HOW_DO_I_TELL_IF_A_SHADER_VARIABLE_IN_A_CONSTANT_BUFFER_ACTUALLY_IS_USED___"></span>How do I tell if a shader variable in a constant buffer actually is used? 
</dt> <dd>

Look at the reflected D3D10\_SHADER\_VARIABLE\_DESC struct for that variable. uFlags should have the D3D10\_SVF\_USED flag set.

</dd> <dt>

<span id="How_do_I_tell_if_a_shader_variable_in_a_constant_buffer_actually_is_using_FX10___"></span><span id="how_do_i_tell_if_a_shader_variable_in_a_constant_buffer_actually_is_using_fx10___"></span><span id="HOW_DO_I_TELL_IF_A_SHADER_VARIABLE_IN_A_CONSTANT_BUFFER_ACTUALLY_IS_USING_FX10___"></span>How do I tell if a shader variable in a constant buffer actually is using FX10? 
</dt> <dd>

This currently is not possible using FX10.

</dd> <dt>

<span id="I_have_no_control_over_constant_buffers_that_FX10_creates._How_are_they_created_and_updated___"></span><span id="i_have_no_control_over_constant_buffers_that_fx10_creates._how_are_they_created_and_updated___"></span><span id="I_HAVE_NO_CONTROL_OVER_CONSTANT_BUFFERS_THAT_FX10_CREATES._HOW_ARE_THEY_CREATED_AND_UPDATED___"></span>I have no control over constant buffers that FX10 creates. How are they created and updated? 
</dt> <dd>

All FX10-managed constant buffers are created as D3D10\_USAGE\_DEFAULT resources and are updated using UpdateSubresource. Because FX10 keeps a backing store of all constant data, UpdateSubresource is the best approach for updating these.

</dd> <dt>

<span id="How_do_I_emulate_the_fixed_function_pipeline_using_shaders___"></span><span id="how_do_i_emulate_the_fixed_function_pipeline_using_shaders___"></span><span id="HOW_DO_I_EMULATE_THE_FIXED_FUNCTION_PIPELINE_USING_SHADERS___"></span>How do I emulate the fixed function pipeline using shaders? 
</dt> <dd>

See FixedFuncEMU sample.

</dd> <dt>

<span id="Should_I_use_the_new__unroll____loop____branch___and_so_on__compiler_hints___"></span><span id="should_i_use_the_new__unroll____loop____branch___and_so_on__compiler_hints___"></span><span id="SHOULD_I_USE_THE_NEW__UNROLL____LOOP____BRANCH___AND_SO_ON__COMPILER_HINTS___"></span>Should I use the new \[unroll\], \[loop\], \[branch\], and so on, compiler hints? 
</dt> <dd>

In general, no. The compiler will often try both ways and choose the fastest one. In some cases, it may be necessary to use \[unroll\], for example, when a texture fetch inside a loop needs access to a gradient.

</dd> <dt>

<span id="Does_partial_precision_make_any_difference_on_D3D10__I_can_specify_partial_precision_in_my_D3D9_HLSL__but_not_in_my_D3D10_HLSL.__"></span><span id="does_partial_precision_make_any_difference_on_d3d10__i_can_specify_partial_precision_in_my_d3d9_hlsl__but_not_in_my_d3d10_hlsl.__"></span><span id="DOES_PARTIAL_PRECISION_MAKE_ANY_DIFFERENCE_ON_D3D10__I_CAN_SPECIFY_PARTIAL_PRECISION_IN_MY_D3D9_HLSL__BUT_NOT_IN_MY_D3D10_HLSL.__"></span>Does partial precision make any difference on D3D10? I can specify partial precision in my D3D9 HLSL, but not in my D3D10 HLSL. 
</dt> <dd>

All D3D10 operations are specified to run at 32-bit floating point precision. Therefore, partial precision should not make any difference in D3D10.

</dd> <dt>

<span id="In_D3D9__I_could_do_HW_PCF_shadow_filtering_by_binding_a_depth_buffer_as_a_texture_and_using_regular_tex2d_hlsl_instructions._How_do_I_do_this_on_D3D10___"></span><span id="in_d3d9__i_could_do_hw_pcf_shadow_filtering_by_binding_a_depth_buffer_as_a_texture_and_using_regular_tex2d_hlsl_instructions._how_do_i_do_this_on_d3d10___"></span><span id="IN_D3D9__I_COULD_DO_HW_PCF_SHADOW_FILTERING_BY_BINDING_A_DEPTH_BUFFER_AS_A_TEXTURE_AND_USING_REGULAR_TEX2D_HLSL_INSTRUCTIONS._HOW_DO_I_DO_THIS_ON_D3D10___"></span>In D3D9, I could do HW PCF shadow filtering by binding a depth buffer as a texture and using regular tex2d hlsl instructions. How do I do this on D3D10? 
</dt> <dd>

You have to use a comparison sampler state and use SampleCmp instructions.

</dd> <dt>

<span id="How_does_this_register_keyword_work_in_D3D10___"></span><span id="how_does_this_register_keyword_work_in_d3d10___"></span><span id="HOW_DOES_THIS_REGISTER_KEYWORD_WORK_IN_D3D10___"></span>How does this register keyword work in D3D10? 
</dt> <dd>

The register keyword in D3D10 now applies to which slot a particular resource is bound to. In this case, the resource can be a Buffer (constant or otherwise), Texture, or Sampler.

-   For constant buffers, use the syntax: register(bN), where N is the input slot (0-15)
-   For textures, use the syntax: register(tN), where N is the input slot (0-127)
-   For samplers, use the syntax: register(sN), where N is the input slot (0-127)

</dd> <dt>

<span id="How_do_I_place_a_variable_inside_a_constant_buffer_if_register_is_just_used_to_specify_where_to_bind_the_entire_buffer___"></span><span id="how_do_i_place_a_variable_inside_a_constant_buffer_if_register_is_just_used_to_specify_where_to_bind_the_entire_buffer___"></span><span id="HOW_DO_I_PLACE_A_VARIABLE_INSIDE_A_CONSTANT_BUFFER_IF_REGISTER_IS_JUST_USED_TO_SPECIFY_WHERE_TO_BIND_THE_ENTIRE_BUFFER___"></span>How do I place a variable inside a constant buffer if register is just used to specify where to bind the entire buffer? 
</dt> <dd>

Use the packoffset keyword. The argument to packoffset is in the form of c\[0-4095\].\[x,y,z,w\]. For example:

``` syntax
        cbuffer cbLotsOfEmptySpace
        {
        float   IWaste2Floats   : packoffset(c0.z);
        float4  IWasteMore  : packoffset(c13);
        };
```

In this constant buffer, IWaste2Floats is placed at the third float (12th byte) in the constant buffer. IWasteMore is placed at the 13th float4 or 52nd float in the constant buffer.

</dd> </dl>

 

 