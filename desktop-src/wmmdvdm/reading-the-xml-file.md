---
title: Reading the XML File
description: Reading the XML File
ms.assetid: '9fda4484-f09d-4ab4-984a-365fb3fffbea'
keywords: ["Windows Movie Maker,reading XML files", "Movie Maker,reading XML files", "Windows DVD Maker,reading XML files", "DVD Maker,reading XML files", "programming guide,reading XML files", "XML,reading XML files", "reading XML files"]
---

# Reading the XML File

The following XML shows a segment of the Windows Movie Maker and Windows DVD Maker private XML file that describes one built-in effect and one built-in transition in Windows Movie Maker. Following the code are brief explanations of some of the key elements and attributes in the XML. Note that both of the transforms highlighted here can be modified, as described in [Making Your Own XML File](making-your-own-xml-file.md).

**Note** This section is intended to give you a feel for the structure and contents of the XML files that Windows Movie Maker parses. It is not intended as a comprehensive guide, nor does it demonstrate any Windows DVD Maker XML content. For a comprehensive overview of the contents of this file and instructions on how to modify it, see [Windows Movie Maker XML Extensibility](windows-movie-maker-xml-extensibility.md). For an overview of the XML content for Windows DVD Maker, see [Windows DVD Maker XML Extensibility](windows-dvd-maker-xml-extensibility.md).

The XML sample that follows defines these two transforms:

-   The "Zoom Out, from Upper Right" effect causes the video clip to begin with the upper-right portion of the picture magnified. As the clip progresses, the focus "zooms" out, giving the appearance of the action receding backward.
-   The "Dissolve" transition causes one clip to fade out at the same time that the next clip is fading in.

**Important** XML file parsing in Windows Movie Maker is case sensitive.


```C++
<TransitionsAndEffects Version="2.8">
    <Transitions>
        <TransitionDLL guid="TFX">
        ...
            <Transition nameID="62816" iconid="38" guid="Dissolve" comment="Dissolve" >
                <Param name="Animation" value="Dissolve" />
                <Param name="DepthBufferFormat" value="75" />
                <Param name="DissolveType" value="Dissolve2D" />
            </Transition>
        ...
        </TransitionDLL>
    </Transitions>
    <Effects>
        <EffectDLL guid="TFX">
        ...
            <Effect nameID="62783" iconid="35" guid="Zoom Out, from Upper Right" comment="Zoom Out, from Upper Right" shadermodel="2">
                <Param name="Animation" value="FXPanZoom" />
                <Param name="FXFile" value="Parity.fx" />
                <Param name="Technique" value="PanZoom" />
                <Semantics>
                    <TextureViewport evaluation="Linear" type="float4">
                        <Point time="0.0" value="0.333334,0.0,0.666666,0.666666"/>
                        <Point time="1.0" value="0.0,0.0,1.0,1.0"/>
                    </TextureViewport>
                </Semantics>
            </Effect>
        ...
        </EffectDLL>
    </Effects>
</TransitionsAndEffects>
```



The following table explains the element tags and attributes in the preceding code. Transitions and effects in Windows Movie Maker use mostly the same tags. Where the tags differ, the table indicates the difference.



<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th>Element</th>
<th>Attributes</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>TransitionsAndEffects</strong></td>

<td>The boundary tag for the whole XML file.</td>
</tr>
<tr class="even">

<td><strong>Version</strong></td>
<td>A required field that should be set to &quot;2.8&quot;.</td>
</tr>
<tr class="odd">
<td><strong>Transitions</strong>-or-<br/> <strong>Effects</strong><br/></td>

<td>This tag bounds the group of all Windows Movie Maker transitions or the group of all Windows Movie Maker effects. Use the appropriate tag for a transition or effect.</td>
</tr>
<tr class="even">
<td><strong>TransitionDLL</strong>-or-<br/> <strong>EffectDLL</strong><br/></td>

<td>This tag bounds a single Windows Movie Maker effect or transition COM object. It can hold one or more custom effects or transitions. Use the appropriate tag for a transition or effect.</td>
</tr>
<tr class="odd">

<td><strong>guid</strong></td>
<td>A required field that lists the GUID defining the transition or effect COM object. (This GUID is actually the ClassID of a COM object that implements the [<strong>IMediaTransform</strong>](imediatransform.md) interface in the underlying code.)If you are using a transition or effect object provided by Movie Maker, this value should be set to &quot;TFX&quot;.<br/></td>
</tr>
<tr class="even">
<td><strong>Transition</strong>-or-<br/> <strong>Effect</strong><br/></td>

<td>This is the boundary tag for an individual Windows Movie Maker transition or effect. One COM object can contain several transitions or effects. (A DLL file can contain several COM objects, although the name of the DLL is not needed for the COM objects that Windows Movie Maker provides.) Use the appropriate tag for a transition or effect.</td>
</tr>
<tr class="odd">

<td><strong>nameID</strong></td>
<td>This is the internal identifier that Windows Movie Maker uses for the transform.When creating your own transform, do not use <strong>nameID</strong>. Instead, when creating your own file, substitute the <strong>name</strong> attribute as shown here:<br/>
<pre data-space="preserve"><code>&lt;Effect 

    name
=&quot;Super Zoom&quot; iconid=&quot;0&quot; guid=&quot;Super Zoom&quot; shadermodel=&quot;2&quot;&gt;</code></pre>
For more information, see [Windows Movie Maker XML Extensibility](windows-movie-maker-xml-extensibility.md).<br/></td>
</tr>
<tr class="even">

<td><strong>iconid</strong></td>
<td>Identifies the icon that Windows Movie Maker displays for the transition.In custom icons, this is a zero-based number indicating which icon in a bitmap strip to use. You can also use one of the existing Windows Movie Maker icons by choosing a number from 1 to approximately 90. For more information on adding custom icons, see [Adding Custom Icons to Windows Movie Maker](adding-custom-icons-to-windows-movie-maker.md).<br/></td>
</tr>
<tr class="odd">

<td><strong>guid</strong></td>
<td>A unique value for this transform.For custom transforms, the only requirement for the value of this attribute is that it be unique among all loaded transforms, both built-in and custom.<br/></td>
</tr>
<tr class="even">

<td><strong>comment</strong></td>
<td>Information ignored by Windows Movie Maker.</td>
</tr>
<tr class="odd">

<td><strong>shadermodel</strong></td>
<td>Specifies which version of the shader model for Windows Movie Maker to use for this transform. All built-in effects use version 2.</td>
</tr>
<tr class="even">
<td><strong>Param</strong></td>

<td>A tag that holds a parameter in the object that you can set. You can have as many <strong>Param</strong> tags as the containing object has parameters.</td>
</tr>
<tr class="odd">

<td><strong>name</strong></td>
<td>The name of the parameter to set.</td>
</tr>
<tr class="even">

<td><strong>value</strong></td>
<td>The value, in quotation marks, to assign to the parameter.</td>
</tr>
<tr class="odd">
<td><strong>Semantics</strong></td>

<td>A tag that defines additional parameters for the transform.</td>
</tr>
</tbody>
</table>



 

## Related topics

<dl> <dt>

[**Creating Custom Transforms Using XML**](creating-custom-transforms-using-xml.md)
</dt> </dl>

 

 





