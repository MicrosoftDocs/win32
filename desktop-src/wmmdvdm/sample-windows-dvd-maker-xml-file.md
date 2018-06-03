---
title: Sample Windows DVD Maker XML File
description: Sample Windows DVD Maker XML File
ms.assetid: 8317be27-4a50-4476-9d2b-5daa8fcec5bd
keywords:
- Windows DVD Maker,sample XML file
- DVD Maker,sample XML file
- programming reference,Windows DVD Maker sample XML file
- reference for Windows DVD Maker,sample XML file
- Windows DVD Maker,transitions
- DVD Maker,transitions
- transitions,sample XML file
- Windows DVD Maker,buttons
- DVD Maker,buttons
- Windows DVD Maker,menus
- DVD Maker,menus
- XML,sample Windows DVD Maker file
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Sample Windows DVD Maker XML File

The following XML code defines one sample transition, one button, and one menu style for Windows DVD Maker. Each element is linked to its corresponding reference page in [Elements](elements.md).

**Notes** The XML provided here is also provided in the file "SampleDVDMenuStyle.xml" in the Media folder of the download provided in [Samples](samples.md). All supplemental resources that are referenced in the code are provided in the Media folder. Use this sample in combination with the reference documentation provided in [Elements](elements.md) as a template from which to create your own custom XML file.

You can create any number of XML files to contain your custom transitions, buttons, and menu styles for Windows DVD Maker, as long as they conform to the guidelines set forth in Step 1 of [Making Your Own XML File](making-your-own-xml-file.md). You can also define custom Windows Movie Maker transforms in the same file.

XML file parsing in Windows DVD Maker is case sensitive.


```C++
<
TransitionsAndEffects Version="2.8">
  <
DVDTransitions>
    <
DVDTransitionDLL guid="{924B0CE7-883F-448a-ADCA-A5E7FDD10E39}">
      <
DVDTransition name="Wavy" iconid="2" guid="Wavy" shadermodel="2">
        <
NumInputs type="int"  value="3" />
        <
Param name="FXFile" value="shader.fx"/>
        <
Param name="Technique" value="SceneButton"/>
      </
DVDTransition>
    </
DVDTransitionDLL>
  </
DVDTransitions>
  <
DVDButtons>
    <
DVDButtonDLL guid="{924B0CE7-883F-448a-ADCA-A5E7FDD10E39}">
      <
DVDButton name="Sample Button" iconid="0" guid="DVDButton-Sample" comment="Sample" shadermodel="2">
        <
StaticThumbnail value="DvdStyles\rectangle_plain_Thumbnail.bmp"/>
        <
FXFile value="shader.fx"/>
        <
Technique value="SceneButton"/>
        <
SubpictureTextures>
          <
Source value="DvdStyles\Circle_SelectionSubpictureB.png"/>
        </
SubpictureTextures>
        <
NumInputs type="int" value="3" />
      </
DVDButton>
    </
DVDButtonDLL>
  </
DVDButtons>
  <
DVDMenuStyles>
    <
DVDMenuStyleDLL guid="TFX">
      <
DVDMenuStyle name="Sample Style" iconid="0" guid="DVDMenu-Sample Style" comment="Sample Style" >
        <
StaticThumbnail value="DvdStyles\Sample\thumbnail.png"/>
        <
GroupName value="Sample Styles" />
        <
SceneButtonTFXToken value="COM\{924B0CE7-883F-448a-ADCA-A5E7FDD10E39}\DVDButton-Sample" />
        <
NavigationButtonTFXToken value="TFX\OverlayImage" />
        <
TextTFXToken value="TFX\DVD Menu Default Text" />
        <
Font value="Segoe UI" />
        <
IsBold value="TRUE" />
        <
FrontColor1 value="#fffffda4" />
        <
TitleText value="My Title" />
        <
PlayButtonText value="My Play" />
        <
Submenu1ButtonText value="My Scenes" />
        <
Submenu2ButtonText value="My Notes" />
        <
UsesBackground value="TRUE" />
        <
Menus >
          <
MainMenu >
            <
ThumbnailTime value="0"/>
            <
Duration value="15000" />
            <
ButtonLocations >
              <
PlayButton value="0.605062, 0.754340, 0.189589, 0.043403" />
              <
Submenu1Button value="0.605062, 0.806424, 0.189589, 0.043403" />
              <
Submenu2Button value="0.605062, 0.858507, 0.189589, 0.043403" />
            </
ButtonLocations>
            <
Graph >
              <
Token value="Pipeline\SolidColor" >
                <
Properties >
                  <
Color value="16777215" />
                </
Properties>
              </
Token>
                <
Input value="InsetVideo" >
                  <
InputStartOffset value="500" />
                  <
MenuStartTime value="0.000000" />
                  <
MenuEndTime value="15000.000000" />
                </
Input>
                <
Token value="COM\{924B0CE7-883F-448a-ADCA-A5E7FDD10E39}\Wavy" >
                  <
MenuStartTime value="0.000000" />
                  <
MenuEndTime value="15000.000000" />
                  <
Properties >
                    <
Scale value="1.000000, 1.000000, 1.000000" />
                    <
Offset value="0.000000, 0.000000, 0.000000" />
                    <
Rotate value="0.000000, 0.000000, 0.000000" />
                    <
Alpha value="1.000000" />
                  </
Properties>
                </
Token>
                <
Text value="Title" >
                  <
Properties >
                    <
FontSize value="18" />
                    <
ResizingTechnique value="AutoResize" />
                    <
MinAutoFontSize value="12" />
                    <
BoundingRect value="0.202674, 0.095920, 0.593696, 0.096354" />
                    <
HorizontalAlignment value="Left" />
                    <
MainPosition value="0.5 0.5" />
                  </
Properties>
                </
Text>
              <
ButtonText value="PlayButton" >
                <
Properties >
                  <
FontSize value="10" />
                  <
BoundingRect value="0.622732, 0.754340, 0.171920, 0.043403" />
                  <
HorizontalAlignment value="Left" />
                  <
MainPosition value="0.5 0.5" />
                </
Properties>
              </
ButtonText>
              <
ButtonText value="Submenu1Button" >
                <
Properties >
                  <
FontSize value="10" />
                  <
BoundingRect value="0.622732, 0.806424, 0.171920, 0.043403" />
                  <
HorizontalAlignment value="Left" />
                  <
MainPosition value="0.5 0.5" />
                </
Properties>
              </
ButtonText>
              <
ButtonText value="Submenu2Button" >
                <
Properties >
                  <
FontSize value="10" />
                  <
BoundingRect value="0.622732, 0.858507, 0.171920, 0.043403" />
                  <
HorizontalAlignment value="Left" />
                  <
MainPosition value="0.5 0.5" />
                </
Properties>
              </
ButtonText>
            </
Graph>
            <
Subpicture >
              <
Token value="Pipeline\SolidColor" >
                <
Properties >
                  <
Color value="16777215" />
                </
Properties>
              </
Token>
              <
NavigationButton value="PlayButton" >
                <
Textures>
                  <
Source value="DvdStyles\Sample\15x15dot.png" />
                </
Textures>
                <
Properties >
                  <
Scale value="0.014327, 0.026042, 1.000000" />
                  <
Offset value="0.224451, -0.552083, 0.000000" />
                  <
Rotate value="0.000000, 0.000000, 0.000000" />
                  <
Alpha value="1.000000" />
                </
Properties>
              </
NavigationButton>
              <
NavigationButton value="Submenu1Button" >
                <
Textures>
                  <
Source value="DvdStyles\Sample\15x15dot.png" />
                </
Textures>
                <
Properties >
                  <
Scale value="0.014327, 0.026042, 1.000000" />
                  <
Offset value="0.224451, -0.656250, 0.000000" />
                  <
Rotate value="0.000000, 0.000000, 0.000000" />
                  <
Alpha value="1.000000" />
                </
Properties>
              </
NavigationButton>
              <
NavigationButton value="Submenu2Button" >
                <
Textures>
                  <
Source value="DvdStyles\Sample\15x15dot.png" />
                </
Textures>
                <
Properties >
                  <
Scale value="0.014327, 0.026042, 1.000000" />
                  <
Offset value="0.224451, -0.760417, 0.000000" />
                  <
Rotate value="0.000000, 0.000000, 0.000000" />
                  <
Alpha value="1.000000" />
                </
Properties>
              </
NavigationButton>
            </
Subpicture>
          </
MainMenu>
          <
MainToNotesTransition >
            <
Duration value="500" />
            <
Graph >
              <
Source value="DvdStyles\Sample\BlackRectangle.bmp" />
              <
Input value="Background" />
              <
Token value="TFX\VideoToFill" >
                <
MenuStartTime value="0.000000" />
                <
MenuEndTime value="500.000000" />
                <
Properties >
                  <
Scale value="1.000000, 1.000000, 1.000000" />
                  <
Offset value="0.000000, 0.000000, 0.000000" />
                  <
Rotate value="0.000000, 0.000000, 0.000000" />
                  <
Alpha value="1.000000" />
                </
Properties>
              </
Token>
              <
Token value="TFX\OverlayImage" >
                <
MenuStartTime value="0.000000" />
                <
MenuEndTime value="500.000000" />
                <
Textures>
                  <
Source value="DvdStyles\Sample\1047x576black.png" />
                </
Textures>
                <
Properties >
                  <
Scale value="1.000000, 1.000000, 1.000000" />
                  <
Offset value="0.000000, 0.000000, 0.000000" />
                  <
Rotate value="0.000000, 0.000000, 0.000000" />
                  <
Alpha value="0.600000" />
                </
Properties>
              </
Token>
              <
Input value="InsetVideo" >
                <
MenuStartTime value="0.000000" />
                <
MenuEndTime value="500.000000" />
              </
Input>
              <
Token value="TFX\VideoToFill" >
                <
MenuStartTime value="0.000000" />
                <
MenuEndTime value="500.000000" />
                <
Properties >
                  <
Scale value="1.000000, 1.000000, 1.000000" />
                  <
Offset value="0.000000, 0.000000, 0.000000" />
                  <
Rotate value="0.000000, 0.000000, 0.000000" />
                  <
Alpha type="float" evaluation="Linear" >
                    <
Point time="0.000000" value="1.000000" />
                    <
Point time="0.966667" value="0.000000" />
                    <
Point time="1.000000" value="0.000000" />
                  </
Alpha>
                </
Properties>
              </
Token>
              <
NavigationButton value="ParentMenuButton" >
                <
MenuStartTime value="0.000000" />
                <
MenuEndTime value="500.000000" />
                <
Textures>
                  <
Source value="DvdStyles\Sample\NavigationUp_ButtonGraphic.png" />
                </
Textures>
                <
Properties >
                  <
Scale value="0.057307, 0.104167, 1.000000" />
                  <
Offset value="0.002865, -0.618056, 0.000000" />
                  <
Rotate value="0.000000, 0.000000, 0.000000" />
                  <
Alpha type="float" evaluation="Linear" >
                    <
Point time="0.000000" value="0.000000" />
                    <
Point time="0.433333" value="0.000000" />
                    <
Point time="0.900000" value="1.000000" />
                    <
Point time="1.000000" value="1.000000" />
                  </
Alpha>
                </
Properties>
              </
NavigationButton>
              <
ButtonText value="Submenu1Button" >
                <
MenuStartTime value="0.000000" />
                <
MenuEndTime value="500.000000" />
                <
Properties >
                  <
FontSize value="10" />
                  <
BoundingRect value="0.622732, 0.806424, 0.171920, 0.043403" />
                  <
HorizontalAlignment value="Left" />
                  <
ExitEffect value="EffectFade" evaluation="Linear" />
                  <
ExitDuration value="0.483333" />
                  <
ExitPosition value="0.500000 0.500000" evaluation="Linear" />
                  <
MainPosition value="0.5 0.5" />
                </
Properties>
              </
ButtonText>
              <
ButtonText value="Submenu2Button" >
                <
MenuStartTime value="0.000000" />
                <
MenuEndTime value="500.000000" />
                <
Properties >
                  <
FontSize value="10" />
                  <
BoundingRect value="0.622732, 0.858507, 0.171920, 0.043403" />
                  <
HorizontalAlignment value="Left" />
                  <
ExitEffect value="EffectFade" evaluation="Linear" />
                  <
ExitDuration value="0.483333" />
                  <
ExitPosition value="0.500000 0.500000" evaluation="Linear" />
                  <
MainPosition value="0.5 0.5" />
                </
Properties>
              </
ButtonText>
              <
ButtonText value="PlayButton" >
                <
MenuStartTime value="0.000000" />
                <
MenuEndTime value="500.000000" />
                <
Properties >
                  <
FontSize value="10" />
                  <
BoundingRect value="0.622732, 0.754340, 0.171920, 0.043403" />
                  <
HorizontalAlignment value="Left" />
                  <
ExitEffect value="EffectFade" evaluation="Linear" />
                  <
ExitDuration value="0.483333" />
                  <
ExitPosition value="0.500000 0.500000" evaluation="Linear" />
                  <
MainPosition value="0.5 0.5" />
                </
Properties>
              </
ButtonText>
              <
Text value="Title" >
                <
MenuStartTime value="0.000000" />
                <
MenuEndTime value="500.000000" />
                <
Properties >
                  <
FontSize value="18" />
                  <
ResizingTechnique value="AutoResize" />
                  <
MinAutoFontSize value="12" />
                  <
BoundingRect value="0.202674, 0.095920, 0.593696, 0.096354" />
                  <
HorizontalAlignment value="Left" />
                  <
ExitEffect value="EffectFade" evaluation="Linear" />
                  <
ExitDuration value="0.483333" />
                  <
ExitPosition value="0.500000 0.500000" evaluation="Linear" />
                  <
MainPosition value="0.5 0.5" />
                </
Properties>
              </
Text>
              <
Text value="Notes" >
                <
MenuStartTime value="0.000000" />
                <
MenuEndTime value="500.000000" />
                <
Properties >
                  <
FontSize value="18" />
                  <
ResizingTechnique value="AutoResize" />
                  <
MinAutoFontSize value="4" />
                  <
BoundingRect value="0.206781, 0.140736, 0.583572, 0.597000" />
                  <
HorizontalAlignment value="Left" />
                  <
EntranceEffect value="EffectFade" evaluation="Linear" />
                  <
EntranceDuration value="0.483333" />
                  <
EntrancePosition value="0.500000 0.500000" evaluation="Linear" />
                  <
MainPosition value="0.5 0.5" />
                </
Properties>
              </
Text>
            </
Graph>
          </
MainToNotesTransition>
          <
MainToScenes2Transition >
            <
Duration value="500" />
            <
Graph >
              <
Source value="DvdStyles\Sample\BlackRectangle.bmp" />
              <
Input value="Background" >
                <
MenuStartTime value="0.000000" />
                <
MenuEndTime value="500.000000" />
              </
Input>
              <
Token value="TFX\VideoToFill" >
                <
MenuStartTime value="0.000000" />
                <
MenuEndTime value="500.000000" />
                <
Properties >
                  <
Scale value="1.000000, 1.000000, 1.000000" />
                  <
Offset value="0.000000, 0.000000, 0.000000" />
                  <
Rotate value="0.000000, 0.000000, 0.000000" />
                  <
Alpha value="1.000000" />
                </
Properties>
              </
Token>
              <
Token value="TFX\OverlayImage" >
                <
MenuStartTime value="0.000000" />
                <
MenuEndTime value="500.000000" />
                <
Textures>
                  <
Source value="DvdStyles\Sample\1047x576black.png" />
                </
Textures>
                <
Properties >
                  <
Scale value="1.000000, 1.000000, 1.000000" />
                  <
Offset value="0.000000, 0.000000, 0.000000" />
                  <
Rotate value="0.000000, 0.000000, 0.000000" />
                  <
Alpha value="0.600000" />
                </
Properties>
              </
Token>
              <
Input value="InsetVideo" >
                <
MenuStartTime value="0.000000" />
                <
MenuEndTime value="500.000000" />
              </
Input>
              <
Token value="TFX\VideoToFill" >
                <
MenuStartTime value="0.000000" />
                <
MenuEndTime value="500.000000" />
                <
Properties >
                  <
Scale value="1.000000, 1.000000, 1.000000" />
                  <
Offset value="0.000000, 0.000000, 0.000000" />
                  <
Rotate value="0.000000, 0.000000, 0.000000" />
                  <
Alpha type="float" evaluation="Linear" >
                    <
Point time="0.000000" value="1.000000" />
                    <
Point time="0.966667" value="0.000000" />
                    <
Point time="1.000000" value="0.000000" />
                  </
Alpha>
                </
Properties>
              </
Token>
              <
NavigationButton value="NextMenuButton" >
                <
MenuStartTime value="0.000000" />
                <
MenuEndTime value="500.000000" />
                <
Textures>
                  <
Source value="DvdStyles\Sample\NavigationRight_ButtonGraphic.png" />
                </
Textures>
                <
Properties >
                  <
Scale value="0.057307, 0.104167, 1.000000" />
                  <
Offset value="0.127030, -0.618056, 0.000000" />
                  <
Rotate value="0.000000, 0.000000, 0.000000" />
                  <
Alpha type="float" evaluation="Linear" >
                    <
Point time="0.000000" value="0.000000" />
                    <
Point time="0.900000" value="1.000000" />
                    <
Point time="1.000000" value="1.000000" />
                  </
Alpha>
                </
Properties>
              </
NavigationButton>
              <
NavigationButton value="ParentMenuButton" >
                <
MenuStartTime value="0.000000" />
                <
MenuEndTime value="500.000000" />
                <
Textures>
                  <
Source value="DvdStyles\Sample\NavigationUp_ButtonGraphic.png" />
                </
Textures>
                <
Properties >
                  <
Scale value="0.057307, 0.104167, 1.000000" />
                  <
Offset value="-0.109838, -0.618056, 0.000000" />
                  <
Rotate value="0.000000, 0.000000, 0.000000" />
                  <
Alpha type="float" evaluation="Linear" >
                    <
Point time="0.000000" value="0.000000" />
                    <
Point time="0.900000" value="1.000000" />
                    <
Point time="1.000000" value="1.000000" />
                  </
Alpha>
                </
Properties>
              </
NavigationButton>
              <
NavigationButton value="PreviousMenuButton" >
                <
MenuStartTime value="0.000000" />
                <
MenuEndTime value="500.000000" />
                <
Textures>
                  <
Source value="DvdStyles\Sample\NavigationLeft_ButtonGraphic.png" />
                </
Textures>
                <
Properties >
                  <
Scale value="0.057307, 0.104167, 1.000000" />
                  <
Offset value="0.008596, -0.618056, 0.000000" />
                  <
Rotate value="0.000000, 0.000000, 0.000000" />
                  <
Alpha type="float" evaluation="Linear" >
                    <
Point time="0.000000" value="0.000000" />
                    <
Point time="0.900000" value="1.000000" />
                    <
Point time="1.000000" value="1.000000" />
                  </
Alpha>
                </
Properties>
              </
NavigationButton>
              <
SceneButton value="Scene1Button" >
                <
MenuStartTime value="0.000000" />
                <
MenuEndTime value="500.000000" />
                <
Properties >
                  <
Scale value="0.220057, 0.300000, 1.000000" />
                  <
Offset type="float3" evaluation="Linear" >
                    <
Point time="0.000000" value="-0.209169, 0.114583, 0.000000" />
                    <
Point time="0.900000" value="-0.209169, 0.114583, 0.000000" />
                    <
Point time="1.000000" value="-0.209169, 0.114583, 0.000000" />
                  </
Offset>
                  <
Rotate type="float3" evaluation="Linear" >
                    <
Point time="0.000000" value="-0.174533, 0.000000, 0.000000" />
                    <
Point time="0.900000" value="0.000000, 0.000000, 0.000000" />
                    <
Point time="1.000000" value="0.000000, 0.000000, 0.000000" />
                  </
Rotate>
                  <
Alpha type="float" evaluation="Linear" >
                    <
Point time="0.000000" value="0.000000" />
                    <
Point time="0.900000" value="1.000000" />
                    <
Point time="1.000000" value="1.000000" />
                  </
Alpha>
                </
Properties>
              </
SceneButton>
              <
SceneButton value="Scene2Button" >
                <
MenuStartTime value="0.000000" />
                <
MenuEndTime value="500.000000" />
                <
Properties >
                  <
Scale value="0.220057, 0.300000, 1.000000" />
                  <
Offset type="float3" evaluation="Linear" >
                    <
Point time="0.000000" value="0.235912, 0.114583, 0.000000" />
                    <
Point time="0.900000" value="0.235912, 0.114583, 0.000000" />
                    <
Point time="1.000000" value="0.235912, 0.114583, 0.000000" />
                  </
Offset>
                  <
Rotate type="float3" evaluation="Linear" >
                    <
Point time="0.000000" value="-0.174533, 0.000000, 0.000000" />
                    <
Point time="0.900000" value="0.000000, 0.000000, 0.000000" />
                    <
Point time="1.000000" value="0.000000, 0.000000, 0.000000" />
                  </
Rotate>
                  <
Alpha type="float" evaluation="Linear" >
                    <
Point time="0.000000" value="0.000000" />
                    <
Point time="0.900000" value="1.000000" />
                    <
Point time="1.000000" value="1.000000" />
                  </
Alpha>
                </
Properties>
              </
SceneButton>
              <
Text value="Title" >
                <
MenuStartTime value="0.000000" />
                <
MenuEndTime value="500.000000" />
                <
Properties >
                  <
FontSize value="18" />
                  <
ResizingTechnique value="AutoResize" />
                  <
MinAutoFontSize value="12" />
                  <
BoundingRect value="0.202674, 0.095920, 0.593696, 0.096354" />
                  <
HorizontalAlignment value="Left" />
                  <
ExitEffect value="EffectFade" evaluation="Linear" />
                  <
ExitDuration value="0.483333" />
                  <
ExitPosition value="0.500000 0.500000" evaluation="Linear" />
                  <
MainPosition value="0.5 0.5" />
                </
Properties>
              </
Text>
              <
ButtonText value="PlayButton" >
                <
MenuStartTime value="0.000000" />
                <
MenuEndTime value="500.000000" />
                <
Properties >
                  <
FontSize value="10" />
                  <
BoundingRect value="0.622732, 0.754340, 0.171920, 0.043403" />
                  <
HorizontalAlignment value="Left" />
                  <
ExitEffect value="EffectFade" evaluation="Linear" />
                  <
ExitDuration value="0.483333" />
                  <
ExitPosition value="0.500000 0.500000" evaluation="Linear" />
                  <
MainPosition value="0.5 0.5" />
                </
Properties>
              </
ButtonText>
              <
ButtonText value="Submenu2Button" >
                <
MenuStartTime value="0.000000" />
                <
MenuEndTime value="500.000000" />
                <
Properties >
                  <
FontSize value="10" />
                  <
BoundingRect value="0.622732, 0.858507, 0.171920, 0.043403" />
                  <
HorizontalAlignment value="Left" />
                  <
ExitEffect value="EffectFade" evaluation="Linear" />
                  <
ExitDuration value="0.483333" />
                  <
ExitPosition value="0.500000 0.500000" evaluation="Linear" />
                  <
MainPosition value="0.5 0.5" />
                </
Properties>
              </
ButtonText>
              <
ButtonText value="Submenu1Button" >
                <
MenuStartTime value="0.000000" />
                <
MenuEndTime value="500.000000" />
                <
Properties >
                  <
FontSize value="10" />
                  <
BoundingRect value="0.622732, 0.806424, 0.171920, 0.043403" />
                  <
HorizontalAlignment value="Left" />
                  <
ExitEffect value="EffectFade" evaluation="Linear" />
                  <
ExitDuration value="0.483333" />
                  <
ExitPosition value="0.500000 0.500000" evaluation="Linear" />
                  <
MainPosition value="0.5 0.5" />
                </
Properties>
              </
ButtonText>
            </
Graph>
          </
MainToScenes2Transition>
          <
MainToScenes4Transition >
            <
Duration value="500" />
            <
Graph >
              <
Source value="DvdStyles\Sample\BlackRectangle.bmp" />
              <
Input value="Background" >
                <
MenuStartTime value="0.000000" />
                <
MenuEndTime value="500.000000" />
              </
Input>
              <
Token value="TFX\VideoToFill" >
                <
MenuStartTime value="0.000000" />
                <
MenuEndTime value="500.000000" />
                <
Properties >
                  <
Scale value="1.000000, 1.000000, 1.000000" />
                  <
Offset value="0.000000, 0.000000, 0.000000" />
                  <
Rotate value="0.000000, 0.000000, 0.000000" />
                  <
Alpha value="1.000000" />
                </
Properties>
              </
Token>
              <
Token value="TFX\OverlayImage" >
                <
MenuStartTime value="0.000000" />
                <
MenuEndTime value="500.000000" />
                <
Textures>
                  <
Source value="DvdStyles\Sample\1047x576black.png" />
                </
Textures>
                <
Properties >
                  <
Scale value="1.000000, 1.000000, 1.000000" />
                  <
Offset value="0.000000, 0.000000, 0.000000" />
                  <
Rotate value="0.000000, 0.000000, 0.000000" />
                  <
Alpha value="0.600000" />
                </
Properties>
              </
Token>
              <
Input value="InsetVideo" >
                <
MenuStartTime value="0.000000" />
                <
MenuEndTime value="500.000000" />
              </
Input>
              <
Token value="TFX\VideoToFill" >
                <
MenuStartTime value="0.000000" />
                <
MenuEndTime value="500.000000" />
                <
Properties >
                  <
Scale value="1.000000, 1.000000, 1.000000" />
                  <
Offset value="0.000000, 0.000000, 0.000000" />
                  <
Rotate value="0.000000, 0.000000, 0.000000" />
                  <
Alpha type="float" evaluation="Linear" >
                    <
Point time="0.000000" value="1.000000" />
                    <
Point time="0.966667" value="0.000000" />
                    <
Point time="1.000000" value="0.000000" />
                  </
Alpha>
                </
Properties>
              </
Token>
              <
NavigationButton value="NextMenuButton" >
                <
MenuStartTime value="0.000000" />
                <
MenuEndTime value="500.000000" />
                <
Textures>
                  <
Source value="DvdStyles\Sample\NavigationRight_ButtonGraphic.png" />
                </
Textures>
                <
Properties >
                  <
Scale value="0.057307, 0.104167, 1.000000" />
                  <
Offset value="0.127030, -0.618056, 0.000000" />
                  <
Rotate value="0.000000, 0.000000, 0.000000" />
                  <
Alpha type="float" evaluation="Linear" >
                    <
Point time="0.000000" value="0.000000" />
                    <
Point time="0.900000" value="1.000000" />
                    <
Point time="1.000000" value="1.000000" />
                  </
Alpha>
                </
Properties>
              </
NavigationButton>
              <
NavigationButton value="ParentMenuButton" >
                <
MenuStartTime value="0.000000" />
                <
MenuEndTime value="500.000000" />
                <
Textures>
                  <
Source value="DvdStyles\Sample\NavigationUp_ButtonGraphic.png" />
                </
Textures>
                <
Properties >
                  <
Scale value="0.057307, 0.104167, 1.000000" />
                  <
Offset value="-0.109838, -0.618056, 0.000000" />
                  <
Rotate value="0.000000, 0.000000, 0.000000" />
                  <
Alpha type="float" evaluation="Linear" >
                    <
Point time="0.000000" value="0.000000" />
                    <
Point time="0.900000" value="1.000000" />
                    <
Point time="1.000000" value="1.000000" />
                  </
Alpha>
                </
Properties>
              </
NavigationButton>
              <
NavigationButton value="PreviousMenuButton" >
                <
MenuStartTime value="0.000000" />
                <
MenuEndTime value="500.000000" />
                <
Textures>
                  <
Source value="DvdStyles\Sample\NavigationLeft_ButtonGraphic.png" />
                </
Textures>
                <
Properties >
                  <
Scale value="0.057307, 0.104167, 1.000000" />
                  <
Offset value="0.008596, -0.618056, 0.000000" />
                  <
Rotate value="0.000000, 0.000000, 0.000000" />
                  <
Alpha type="float" evaluation="Linear" >
                    <
Point time="0.000000" value="0.000000" />
                    <
Point time="0.900000" value="1.000000" />
                    <
Point time="1.000000" value="1.000000" />
                  </
Alpha>
                </
Properties>
              </
NavigationButton>
              <
SceneButton value="Scene1Button" >
                <
MenuStartTime value="0.000000" />
                <
MenuEndTime value="500.000000" />
                <
Properties >
                  <
Scale value="0.220057, 0.300000, 1.000000" />
                  <
Offset type="float3" evaluation="Linear" >
                    <
Point time="0.000000" value="-0.209169, 0.416667, 0.000000" />
                    <
Point time="0.900000" value="-0.209169, 0.416667, 0.000000" />
                    <
Point time="1.000000" value="-0.209169, 0.416667, 0.000000" />
                  </
Offset >
                  <
Rotate type="float3" evaluation="Linear" >
                    <
Point time="0.000000" value="-0.174533, 0.000000, 0.000000" />
                    <
Point time="0.900000" value="0.000000, 0.000000, 0.000000" />
                    <
Point time="1.000000" value="0.000000, 0.000000, 0.000000" />
                  </
Rotate>
                  <
Alpha type="float" evaluation="Linear" >
                    <
Point time="0.000000" value="0.000000" />
                    <
Point time="0.900000" value="1.000000" />
                    <
Point time="1.000000" value="1.000000" />
                  </
Alpha>
                </
Properties>
              </
SceneButton>
              <
SceneButton value="Scene2Button" >
                <
MenuStartTime value="0.000000" />
                <
MenuEndTime value="500.000000" />
                <
Properties >
                  <
Scale value="0.220057, 0.300000, 1.000000" />
                  <
Offset type="float3" evaluation="Linear" >
                    <
Point time="0.000000" value="0.235912, 0.416667, 0.000000" />
                    <
Point time="0.900000" value="0.235912, 0.416667, 0.000000" />
                    <
Point time="1.000000" value="0.235912, 0.416667, 0.000000" />
                  </
Offset>
                  <
Rotate type="float3" evaluation="Linear" >
                    <
Point time="0.000000" value="-0.174533, 0.000000, 0.000000" />
                    <
Point time="0.900000" value="0.000000, 0.000000, 0.000000" />
                    <
Point time="1.000000" value="0.000000, 0.000000, 0.000000" />
                  </
Rotate>
                  <
Alpha type="float" evaluation="Linear" >
                    <
Point time="0.000000" value="0.000000" />
                    <
Point time="0.900000" value="1.000000" />
                    <
Point time="1.000000" value="1.000000" />
                  </
Alpha>
                </
Properties>
              </
SceneButton>
              <
SceneButton value="Scene3Button" >
                <
MenuStartTime value="0.000000" />
                <
MenuEndTime value="500.000000" />
                <
Properties >
                  <
Scale value="0.220057, 0.300000, 1.000000" />
                  <
Offset type="float3" evaluation="Linear" >
                    <
Point time="0.000000" value="-0.209169, -0.190972, 0.000000" />
                    <
Point time="0.900000" value="-0.209169, -0.190972, 0.000000" />
                    <
Point time="1.000000" value="-0.209169, -0.190972, 0.000000" />
                  </
Offset>
                  <
Rotate type="float3" evaluation="Linear" >
                    <
Point time="0.000000" value="-0.174533, 0.000000, 0.000000" />
                    <
Point time="0.900000" value="0.000000, 0.000000, 0.000000" />
                    <
Point time="1.000000" value="0.000000, 0.000000, 0.000000" />
                  </
Rotate>
                  <
Alpha type="float" evaluation="Linear" >
                    <
Point time="0.000000" value="0.000000" />
                    <
Point time="0.900000" value="1.000000" />
                    <
Point time="1.000000" value="1.000000" />
                  </
Alpha>
                </
Properties>
              </
SceneButton>
              <
SceneButton value="Scene4Button" >
                <
MenuStartTime value="0.000000" />
                <
MenuEndTime value="500.000000" />
                <
Properties >
                  <
Scale value="0.220057, 0.300000, 1.000000" />
                  <
Offset type="float3" evaluation="Linear" >
                    <
Point time="0.000000" value="0.235912, -0.190972, 0.000000" />
                    <
Point time="0.900000" value="0.235912, -0.190972, 0.000000" />
                    <
Point time="1.000000" value="0.235912, -0.190972, 0.000000" />
                  </
Offset>
                  <
Rotate type="float3" evaluation="Linear" >
                    <
Point time="0.000000" value="-0.174533, 0.000000, 0.000000" />
                    <
Point time="0.900000" value="0.000000, 0.000000, 0.000000" />
                    <
Point time="1.000000" value="0.000000, 0.000000, 0.000000" />
                  </
Rotate>
                  <
Alpha type="float" evaluation="Linear" >
                    <
Point time="0.000000" value="0.000000" />
                    <
Point time="0.900000" value="1.000000" />
                    <
Point time="1.000000" value="1.000000" />
                  </
Alpha>
                </
Properties>
              </
SceneButton>
              <
ButtonText value="Submenu1Button" >
                <
MenuStartTime value="0.000000" />
                <
MenuEndTime value="500.000000" />
                <
Properties >
                  <
FontSize value="10" />
                  <
BoundingRect value="0.622732, 0.806424, 0.171920, 0.043403" />
                  <
HorizontalAlignment value="Left" />
                  <
ExitEffect value="EffectFade" evaluation="Linear" />
                  <
ExitDuration value="0.483333" />
                  <
ExitPosition value="0.500000 0.500000" evaluation="Linear" />
                  <
MainPosition value="0.5 0.5" />
                </
Properties>
              </
ButtonText>
              <
ButtonText value="Submenu2Button" >
                <
MenuStartTime value="0.000000" />
                <
MenuEndTime value="500.000000" />
                <
Properties >
                  <
FontSize value="10" />
                  <
BoundingRect value="0.622732, 0.858507, 0.171920, 0.043403" />
                  <
HorizontalAlignment value="Left" />
                  <
ExitEffect value="EffectFade" evaluation="Linear" />
                  <
ExitDuration value="0.483333" />
                  <
ExitPosition value="0.500000 0.500000" evaluation="Linear" />
                  <
MainPosition value="0.5 0.5" />
                </
Properties>
              </
ButtonText>
              <
ButtonText value="PlayButton" >
                <
MenuStartTime value="0.000000" />
                <
MenuEndTime value="500.000000" />
                <
Properties >
                  <
FontSize value="10" />
                  <
BoundingRect value="0.622732, 0.754340, 0.171920, 0.043403" />
                  <
HorizontalAlignment value="Left" />
                  <
ExitEffect value="EffectFade" evaluation="Linear" />
                  <
ExitDuration value="0.483333" />
                  <
ExitPosition value="0.500000 0.500000" evaluation="Linear" />
                  <
MainPosition value="0.5 0.5" />
                </
Properties>
              </
ButtonText>
              <
Text value="Title" >
                <
MenuStartTime value="0.000000" />
                <
MenuEndTime value="500.000000" />
                <
Properties >
                  <
FontSize value="18" />
                  <
ResizingTechnique value="AutoResize" />
                  <
MinAutoFontSize value="12" />
                  <
BoundingRect value="0.202674, 0.095920, 0.593696, 0.096354" />
                  <
HorizontalAlignment value="Left" />
                  <
ExitEffect value="EffectFade" evaluation="Linear" />
                  <
ExitDuration value="0.483333" />
                  <
ExitPosition value="0.500000 0.500000" evaluation="Linear" />
                  <
MainPosition value="0.5 0.5" />
                </
Properties>
              </
Text>
            </
Graph>
          </
MainToScenes4Transition>
          <
NotesMenu >
            <
Duration value="15000" />
            <
ThumbnailTime value="0"/>
            <
ButtonLocations >
              <
ParentMenuButton value="0.472779, 0.756944, 0.057307, 0.104167" />
            </
ButtonLocations>
            <
Graph >
              <
Source value="DvdStyles\Sample\BlackRectangle.bmp" />
              <
Input value="Background" >
                <
InputStartOffset value="500.000000" />
                <
MenuStartTime value="0.000000" />
                <
MenuEndTime value="15000.000000" />
              </
Input>
              <
Token value="TFX\VideoToFill" >
                <
MenuStartTime value="0.000000" />
                <
MenuEndTime value="15000.000000" />
                <
Properties >
                  <
Scale value="1.000000, 1.000000, 1.000000" />
                  <
Offset value="0.000000, 0.000000, 0.000000" />
                  <
Rotate value="0.000000, 0.000000, 0.000000" />
                  <
Alpha value="1.000000" />
                </
Properties>
              </
Token>
              <
Token value="TFX\OverlayImage" >
                <
MenuStartTime value="0.000000" />
                <
MenuEndTime value="15000.000000" />
                <
Textures>
                  <
Source value="DvdStyles\Sample\1047x576black.png" />
                </
Textures>
                <
Properties >
                  <
Scale value="1.000000, 1.000000, 1.000000" />
                  <
Offset value="0.000000, 0.000000, 0.000000" />
                  <
Rotate value="0.000000, 0.000000, 0.000000" />
                  <
Alpha value="0.600000" />
                </
Properties>
              </
Token>
              <
NavigationButton value="ParentMenuButton" >
                <
MenuStartTime value="0.000000" />
                <
MenuEndTime value="15000.000000" />
                <
Textures>
                  <
Source value="DvdStyles\Sample\NavigationUp_ButtonGraphic.png" />
                </
Textures>
                <
Properties >
                  <
Scale value="0.057307, 0.104167, 1.000000" />
                  <
Offset value="0.002865, -0.618056, 0.000000" />
                  <
Rotate value="0.000000, 0.000000, 0.000000" />
                  <
Alpha value="1.000000" />
                </
Properties>
              </
NavigationButton>
              <
Text value="Notes" >
                <
MenuStartTime value="0.000000" />
                <
MenuEndTime value="15000.000000" />
                <
Properties >
                  <
FontSize value="18" />
                  <
ResizingTechnique value="AutoResize" />
                  <
MinAutoFontSize value="4" />
                  <
BoundingRect value="0.206781, 0.140625, 0.583572, 0.597222" />
                  <
HorizontalAlignment value="Left" />
                  <
MainPosition value="0.5 0.5" />
                </
Properties>
              </
Text>
            </
Graph>
            <
Subpicture >
              <
Token value="Pipeline\SolidColor" >
                <
Properties >
                  <
Color value="16777215" />
                </
Properties>
              </
Token>
              <
NavigationButton value="ParentMenuButton" >
                <
MenuStartTime value="0.000000" />
                <
MenuEndTime value="15000.000000" />
                <
Textures>
                  <
Source value="DvdStyles\Sample\NavigationUp_SelectionSubpicture.png" />
                </
Textures>
                <
Properties >
                  <
Scale value="0.057307, 0.104167, 1.000000" />
                  <
Offset value="0.002865, -0.618056, 0.000000" />
                  <
Rotate value="0.000000, 0.000000, 0.000000" />
                  <
Alpha value="1.000000" />
                </
Properties>
              </
NavigationButton>
            </
Subpicture>
          </
NotesMenu>
          <
ScenesMenu2 >
            <
ThumbnailTime value="0"/>
            <
Duration value="15000" />
            <
ButtonLocations >
              <
NextMenuButton value="0.534862, 0.756944, 0.057307, 0.104167" />
              <
ParentMenuButton value="0.416428, 0.756944, 0.057307, 0.104167" />
              <
PreviousMenuButton value="0.475645, 0.756944, 0.057307, 0.104167" />
              <
Scene1Button value="0.285387, 0.292708, 0.220057, 0.300000" />
              <
Scene2Button value="0.507927, 0.292708, 0.220057, 0.300000" />
            </
ButtonLocations>
            <
Graph >
              <
Source value="DvdStyles\Sample\BlackRectangle.bmp" />
              <
Input value="Background" >
                <
InputStartOffset value="500.000000" />
                <
MenuStartTime value="0.000000" />
                <
MenuEndTime value="15000.000000" />
              </
Input >
              <
Token value="TFX\VideoToFill" >
                <
MenuStartTime value="0.000000" />
                <
MenuEndTime value="15000.000000" />
                <
Properties >
                  <
Scale value="1.000000, 1.000000, 1.000000" />
                  <
Offset value="0.000000, 0.000000, 0.000000" />
                  <
Rotate value="0.000000, 0.000000, 0.000000" />
                  <
Alpha value="1.000000" />
                </
Properties>
              </
Token>
              <
Textures>
                <
Source value="DvdStyles\Sample\1047x576black.png" />
              </
Textures>
              <
Token value="TFX\OverlayImage" >
                <
MenuStartTime value="0.000000" />
                <
MenuEndTime value="15000.000000" />
                <
Properties >
                  <
Scale value="1.000000, 1.000000, 1.000000" />
                  <
Offset value="0.000000, 0.000000, 0.000000" />
                  <
Rotate value="0.000000, 0.000000, 0.000000" />
                  <
Alpha value="0.600000" />
                </
Properties>
              </
Token>
              <
NavigationButton value="NextMenuButton" >
                <
MenuStartTime value="0.000000" />
                <
MenuEndTime value="15000.000000" />
                <
Textures>
                  <
Source value="DvdStyles\Sample\NavigationRight_ButtonGraphic.png" />
                </
Textures>
                <
Properties >
                  <
Scale value="0.057307, 0.104167, 1.000000" />
                  <
Offset value="0.127030, -0.618056, 0.000000" />
                  <
Rotate value="0.000000, 0.000000, 0.000000" />
                  <
Alpha value="1.000000" />
                </
Properties>
              </
NavigationButton>
              <
NavigationButton value="ParentMenuButton" >
                <
MenuStartTime value="0.000000" />
                <
MenuEndTime value="15000.000000" />
                <
Textures>
                  <
Source value="DvdStyles\Sample\NavigationUp_ButtonGraphic.png" />
                </
Textures>
                <
Properties >
                  <
Scale value="0.057307, 0.104167, 1.000000" />
                  <
Offset value="-0.109838, -0.618056, 0.000000" />
                  <
Rotate value="0.000000, 0.000000, 0.000000" />
                  <
Alpha value="1.000000" />
                </
Properties>
              </
NavigationButton>
              <
NavigationButton value="PreviousMenuButton" >
                <
MenuStartTime value="0.000000" />
                <
MenuEndTime value="15000.000000" />
                <
Textures>
                  <
Source  value="DvdStyles\Sample\NavigationLeft_ButtonGraphic.png" />
                </
Textures>
                <
Properties >
                  <
Scale value="0.057307, 0.104167, 1.000000" />
                  <
Offset value="0.008596, -0.618056, 0.000000" />
                  <
Rotate value="0.000000, 0.000000, 0.000000" />
                  <
Alpha value="1.000000" />
                </
Properties>
              </
NavigationButton>
              <
SceneButton value="Scene1Button" >
                <
MenuStartTime value="0.000000" />
                <
MenuEndTime value="15000.000000" />
                <
InputStartOffset value="500.000000" />
                <
Properties >
                  <
Scale value="0.220057, 0.300000, 1.000000" />
                  <
Offset value="-0.209169, 0.114583, 0.000000" />
                  <
Rotate value="0.000000, 0.000000, 0.000000" />
                  <
Alpha value="1.000000" />
                </
Properties>
              </
SceneButton>
              <
SceneButton value="Scene2Button" >
                <
MenuStartTime value="0.000000" />
                <
MenuEndTime value="15000.000000" />
                <
InputStartOffset value="500.000000" />
                <
Properties >
                  <
Scale  value="0.220057, 0.300000, 1.000000" />
                  <
Offset value="0.235912, 0.114583, 0.000000" />
                  <
Rotate value="0.000000, 0.000000, 0.000000" />
                  <
Alpha value="1.000000" />
                </
Properties>
              </
SceneButton>
            </
Graph>
            <
Subpicture >
              <
Token value="Pipeline\SolidColor" >
                <
Properties >
                  <
Color value="16777215" />
                </
Properties>
              </
Token>
              <
NavigationButton value="NextMenuButton" >
                <
MenuStartTime value="0.000000" />
                <
MenuEndTime value="15000.000000" />
                <
Textures>
                  <
Source  value="DvdStyles\Sample\NavigationRight_SelectionSubpicture.png" />
                </
Textures>
                <
Properties >
                  <
Scale  value="0.057307, 0.104167, 1.000000" />
                  <
Offset value="0.127030, -0.618056, 0.000000" />
                  <
Rotate value="0.000000, 0.000000, 0.000000" />
                  <
Alpha value="1.000000" />
                </
Properties>
              </
NavigationButton>
              <
NavigationButton value="ParentMenuButton" >
                <
MenuStartTime value="0.000000" />
                <
MenuEndTime value="15000.000000" />
                <
Textures>
                  <
Source  value="DvdStyles\Sample\NavigationUp_SelectionSubpicture.png" />
                </
Textures>
                <
Properties >
                  <
Scale  value="0.057307, 0.104167, 1.000000" />
                  <
Offset value="-0.109838, -0.618056, 0.000000" />
                  <
Rotate value="0.000000, 0.000000, 0.000000" />
                  <
Alpha value="1.000000" />
                </
Properties>
              </
NavigationButton>
              <
NavigationButton value="PreviousMenuButton" >
                <
MenuStartTime value="0.000000" />
                <
MenuEndTime value="15000.000000" />
                <
Textures>
                  <
Source  value="DvdStyles\Sample\NavigationLeft_SelectionSubpicture.png" />
                </
Textures>
                <
Properties >
                  <
Scale  value="0.057307, 0.104167, 1.000000" />
                  <
Offset value="0.008596, -0.618056, 0.000000" />
                  <
Rotate value="0.000000, 0.000000, 0.000000" />
                  <
Alpha value="1.000000" />
                </
Properties>
              </
NavigationButton>
              <
SceneButton value="Scene1Button" >
                <
MenuStartTime value="0.000000" />
                <
MenuEndTime value="15000.000000" />
                <
InputStartOffset value="500.000000" />
                <
Properties >
                  <
ButtonSelection value="TRUE" />
                  <
Scale  value="0.220057, 0.300000, 1.000000" />
                  <
Offset value="-0.209169, 0.114583, 0.000000" />
                  <
Rotate value="0.000000, 0.000000, 0.000000" />
                  <
Alpha value="1.000000" />
                </
Properties>
              </
SceneButton>
              <
SceneButton value="Scene2Button" >
                <
MenuStartTime value="0.000000" />
                <
MenuEndTime value="15000.000000" />
                <
InputStartOffset value="500.000000" />
                <
Properties >
                  <
ButtonSelection value="TRUE" />
                  <
Scale  value="0.220057, 0.300000, 1.000000" />
                  <
Offset value="0.235912, 0.114583, 0.000000" />
                  <
Rotate value="0.000000, 0.000000, 0.000000" />
                  <
Alpha value="1.000000" />
                </
Properties>
              </
SceneButton>
            </
Subpicture>
          </
ScenesMenu2>
          <
ScenesMenu4 >
            <
ThumbnailTime value="0"/>
            <
Duration value="15000" />
            <
ButtonLocations >
              <
NextMenuButton value="0.534862, 0.756944, 0.057307, 0.104167" />
              <
ParentMenuButton value="0.416428, 0.756944, 0.057307, 0.104167" />
              <
PreviousMenuButton value="0.475645, 0.756944, 0.057307, 0.104167" />
              <
Scene1Button value="0.285387, 0.141667, 0.220057, 0.300000" />
              <
Scene2Button value="0.507927, 0.141667, 0.220057, 0.300000" />
              <
Scene3Button value="0.285387, 0.445486, 0.220057, 0.300000" />
              <
Scene4Button value="0.507927, 0.445486, 0.220057, 0.300000" />
            </
ButtonLocations>
            <
Graph >
              <
Source value="DvdStyles\Sample\BlackRectangle.bmp" />
              <
Input value="Background" >
                <
InputStartOffset value="500.000000" />
                <
MenuStartTime value="0.000000" />
                <
MenuEndTime value="15000.000000" />
              </
Input>
              <
Token value="TFX\VideoToFill" >
                <
MenuStartTime value="0.000000" />
                <
MenuEndTime value="15000.000000" />
                <
Properties >
                  <
Scale  value="1.000000, 1.000000, 1.000000" />
                  <
Offset value="0.000000, 0.000000, 0.000000" />
                  <
Rotate value="0.000000, 0.000000, 0.000000" />
                  <
Alpha value="1.000000" />
                </
Properties>
              </
Token>
              <
Token value="TFX\OverlayImage" >
                <
MenuStartTime value="0.000000" />
                <
MenuEndTime value="15000.000000" />
                <
Textures>
                  <
Source value="DvdStyles\Sample\1047x576black.png" />
                </
Textures>
                <
Properties >
                  <
Scale  value="1.000000, 1.000000, 1.000000" />
                  <
Offset value="0.000000, 0.000000, 0.000000" />
                  <
Rotate value="0.000000, 0.000000, 0.000000" />
                  <
Alpha value="0.600000" />
                </
Properties>
              </
Token>
              <
NavigationButton value="NextMenuButton" >
                <
MenuStartTime value="0.000000" />
                <
MenuEndTime value="15000.000000" />
                <
Textures>
                  <
Source value="DvdStyles\Sample\NavigationRight_ButtonGraphic.png" />
                </
Textures>
                <
Properties >
                  <
Scale  value="0.057307, 0.104167, 1.000000" />
                  <
Offset value="0.127030, -0.618056, 0.000000" />
                  <
Rotate value="0.000000, 0.000000, 0.000000" />
                  <
Alpha value="1.000000" />
                </
Properties>
              </
NavigationButton>
              <
NavigationButton value="ParentMenuButton" >
                <
MenuStartTime value="0.000000" />
                <
MenuEndTime value="15000.000000" />
                <
Textures>
                  <
Source value="DvdStyles\Sample\NavigationUp_ButtonGraphic.png" />
                </
Textures>
                <
Properties >
                  <
Scale  value="0.057307, 0.104167, 1.000000" />
                  <
Offset value="-0.109838, -0.618056, 0.000000" />
                  <
Rotate value="0.000000, 0.000000, 0.000000" />
                  <
Alpha value="1.000000" />
                </
Properties>
              </
NavigationButton>
              <
NavigationButton value="PreviousMenuButton" >
                <
MenuStartTime value="0.000000" />
                <
MenuEndTime value="15000.000000" />
                <
Textures>
                  <
Source value="DvdStyles\Sample\NavigationLeft_ButtonGraphic.png" />
                </
Textures>
                <
Properties >
                  <
Scale  value="0.057307, 0.104167, 1.000000" />
                  <
Offset value="0.008596, -0.618056, 0.000000" />
                  <
Rotate value="0.000000, 0.000000, 0.000000" />
                  <
Alpha value="1.000000" />
                </
Properties>
              </
NavigationButton>
              <
SceneButton value="Scene1Button" >
                <
MenuStartTime value="0.000000" />
                <
MenuEndTime value="15000.000000" />
                <
InputStartOffset value="500.000000" />
                <
Properties >
                  <
Scale  value="0.220057, 0.300000, 1.000000" />
                  <
Offset value="-0.209169, 0.416667, 0.000000" />
                  <
Rotate value="0.000000, 0.000000, 0.000000" />
                  <
Alpha value="1.000000" />
                </
Properties>
              </
SceneButton>
              <
SceneButton value="Scene2Button" >
                <
MenuStartTime value="0.000000" />
                <
MenuEndTime value="15000.000000" />
                <
InputStartOffset value="500.000000" />
                <
Properties >
                  <
Scale  value="0.220057, 0.300000, 1.000000" />
                  <
Offset value="0.235912, 0.416667, 0.000000" />
                  <
Rotate value="0.000000, 0.000000, 0.000000" />
                  <
Alpha value="1.000000" />
                </
Properties>
              </
SceneButton>
              <
SceneButton value="Scene3Button" >
                <
MenuStartTime value="0.000000" />
                <
MenuEndTime value="15000.000000" />
                <
InputStartOffset value="500.000000" />
                <
Properties >
                  <
Scale  value="0.220057, 0.300000, 1.000000" />
                  <
Offset value="-0.209169, -0.190972, 0.000000" />
                  <
Rotate value="0.000000, 0.000000, 0.000000" />
                  <
Alpha value="1.000000" />
                </
Properties>
              </
SceneButton>
              <
SceneButton value="Scene4Button" >
                <
MenuStartTime value="0.000000" />
                <
MenuEndTime value="15000.000000" />
                <
InputStartOffset value="500.000000" />
                <
Properties >
                  <
Scale  value="0.220057, 0.300000, 1.000000" />
                  <
Offset value="0.235912, -0.190972, 0.000000" />
                  <
Rotate value="0.000000, 0.000000, 0.000000" />
                  <
Alpha value="1.000000" />
                </
Properties>
              </
SceneButton>
            </
Graph>
            <
Subpicture >
              <
Token value="Pipeline\SolidColor" >
                <
Properties >
                  <
Color value="16777215" />
                </
Properties>
              </
Token>
              <
NavigationButton value="NextMenuButton" >
                <
MenuStartTime value="0.000000" />
                <
MenuEndTime value="15000.000000" />
                <
Textures>
                  <
Source value="DvdStyles\Sample\NavigationRight_SelectionSubpicture.png" />
                </
Textures>
                <
Properties >
                  <
Scale  value="0.057307, 0.104167, 1.000000" />
                  <
Offset value="0.127030, -0.618056, 0.000000" />
                  <
Rotate value="0.000000, 0.000000, 0.000000" />
                  <
Alpha value="1.000000" />
                </
Properties>
              </
NavigationButton>
              <
NavigationButton value="ParentMenuButton" >
                <
MenuStartTime value="0.000000" />
                <
MenuEndTime value="15000.000000" />
                <
Textures>
                  <
Source value="DvdStyles\Sample\NavigationUp_SelectionSubpicture.png" />
                </
Textures>
                <
Properties >
                  <
Scale  value="0.057307, 0.104167, 1.000000" />
                  <
Offset value="-0.109838, -0.618056, 0.000000" />
                  <
Rotate value="0.000000, 0.000000, 0.000000" />
                  <
Alpha value="1.000000" />
                </
Properties>
              </
NavigationButton>
              <
NavigationButton value="PreviousMenuButton" >
                <
MenuStartTime value="0.000000" />
                <
MenuEndTime value="15000.000000" />
                <
Textures>
                  <
Source value="DvdStyles\Sample\NavigationLeft_SelectionSubpicture.png" />
                </
Textures>
                <
Properties >
                  <
Scale  value="0.057307, 0.104167, 1.000000" />
                  <
Offset value="0.008596, -0.618056, 0.000000" />
                  <
Rotate value="0.000000, 0.000000, 0.000000" />
                  <
Alpha value="1.000000" />
                </
Properties>
              </
NavigationButton>
              <
SceneButton value="Scene1Button" >
                <
MenuStartTime value="0.000000" />
                <
MenuEndTime value="15000.000000" />
                <
InputStartOffset value="500.000000" />
                <
Properties >
                  <
ButtonSelection value="TRUE" />
                  <
Scale  value="0.220057, 0.300000, 1.000000" />
                  <
Offset value="-0.209169, 0.416667, 0.000000" />
                  <
Rotate value="0.000000, 0.000000, 0.000000" />
                  <
Alpha value="1.000000" />
                </
Properties>
              </
SceneButton>
              <
SceneButton value="Scene2Button" >
                <
MenuStartTime value="0.000000" />
                <
MenuEndTime value="15000.000000" />
                <
InputStartOffset value="500.000000" />
                <
Properties >
                  <
ButtonSelection value="TRUE" />
                  <
Scale  value="0.220057, 0.300000, 1.000000" />
                  <
Offset value="0.235912, 0.416667, 0.000000" />
                  <
Rotate value="0.000000, 0.000000, 0.000000" />
                  <
Alpha value="1.000000" />
                </
Properties>
              </
SceneButton>
              <
SceneButton value="Scene3Button" >
                <
MenuStartTime value="0.000000" />
                <
MenuEndTime value="15000.000000" />
                <
InputStartOffset value="500.000000" />
                <
Properties >
                  <
ButtonSelection value="TRUE" />
                  <
Scale  value="0.220057, 0.300000, 1.000000" />
                  <
Offset value="-0.209169, -0.190972, 0.000000" />
                  <
Rotate value="0.000000, 0.000000, 0.000000" />
                  <
Alpha value="1.000000" />
                </
Properties>
              </
SceneButton>
              <
SceneButton value="Scene4Button" >
                <
MenuStartTime value="0.000000" />
                <
MenuEndTime value="15000.000000" />
                <
InputStartOffset value="500.000000" />
                <
Properties >
                  <
ButtonSelection value="TRUE" />
                  <
Scale  value="0.220057, 0.300000, 1.000000" />
                  <
Offset value="0.235912, -0.190972, 0.000000" />
                  <
Rotate value="0.000000, 0.000000, 0.000000" />
                  <
Alpha value="1.000000" />
                </
Properties>
              </
SceneButton>
            </
Subpicture>
          </
ScenesMenu4>
          <
ScenesMenu6 >
            <
ThumbnailTime value="0"/>
            <
Duration value="15000" />
            <
ButtonLocations >
              <
NextMenuButton value="0.531996, 0.756944, 0.057307, 0.104167" />
              <
ParentMenuButton value="0.413563, 0.756944, 0.057307, 0.104167" />
              <
PreviousMenuButton value="0.472779, 0.756944, 0.057307, 0.104167" />
              <
Scene1Button value="0.179561, 0.151042, 0.206304, 0.281250" />
              <
Scene2Button value="0.396371, 0.151042, 0.206304, 0.281250" />
              <
Scene3Button value="0.613181, 0.151042, 0.206304, 0.281250" />
              <
Scene4Button value="0.179561, 0.454861, 0.206304, 0.281250" />
              <
Scene5Button value="0.396371, 0.454861, 0.206304, 0.281250" />
              <
Scene6Button value="0.613181, 0.454861, 0.206304, 0.281250" />
            </
ButtonLocations>
            <
Graph >
              <
Source value="DvdStyles\BlackRectangle.bmp" />
              <
Input value="Background" >
                <
InputStartOffset value="500.000000" />
                <
MenuStartTime value="0.000000" />
                <
MenuEndTime value="15000.000000" />
              </
Input>
              <
Token value="TFX\VideoToFill" >
                <
MenuStartTime value="0.000000" />
                <
MenuEndTime value="15000.000000" />
                <
Properties >
                  <
Scale  value="1.000000, 1.000000, 1.000000" />
                  <
Offset value="0.000000, 0.000000, 0.000000" />
                  <
Rotate value="0.000000, 0.000000, 0.000000" />
                  <
Alpha value="1.00000" />
                </
Properties>
              </
Token>
              <
Token value="TFX\OverlayImage" >
                <
MenuStartTime value="0.000000" />
                <
MenuEndTime value="15000.000000" />
                <
Textures>
                  <
Source value="DvdStyles\Sample\1047x576black.png" />
                </
Textures>
                <
Properties >
                  <
Scale  value="1.000000, 1.000000, 1.000000" />
                  <
Offset value="0.000000, 0.000000, 0.000000" />
                  <
Rotate value="0.000000, 0.000000, 0.000000" />
                  <
Alpha value="0.600000" />
                </
Properties>
              </
Token>
              <
NavigationButton value="NextMenuButton" >
                <
MenuStartTime value="0.000000" />
                <
MenuEndTime value="15000.000000" />
                <
Textures>
                  <
Source value="DvdStyles\Sample\NavigationRight_ButtonGraphic.png" />
                </
Textures>
                <
Properties >
                  <
Scale  value="0.057307, 0.104167, 1.000000" />
                  <
Offset value="0.121299, -0.618056, 0.000000" />
                  <
Rotate value="0.000000, 0.000000, 0.000000" />
                  <
Alpha value="1.000000" />
                </
Properties>
              </
NavigationButton>
              <
NavigationButton value="ParentMenuButton" >
                <
MenuStartTime value="0.000000" />
                <
MenuEndTime value="15000.000000" />
                <
Textures>
                  <
Source value="DvdStyles\Sample\NavigationUp_ButtonGraphic.png" />
                </
Textures>
                <
Properties >
                  <
Scale  value="0.057307, 0.104167, 1.000000" />
                  <
Offset value="-0.115568, -0.618056, 0.000000" />
                  <
Rotate value="0.000000, 0.000000, 0.000000" />
                  <
Alpha value="1.000000" />
                </
Properties>
              </
NavigationButton>
              <
NavigationButton value="PreviousMenuButton" >
                <
MenuStartTime value="0.000000" />
                <
MenuEndTime value="15000.000000" />
                <
Textures>
                  <
Source value="DvdStyles\Sample\NavigationLeft_ButtonGraphic.png" />
                </
Textures>
                <
Properties >
                  <
Scale  value="0.057307, 0.104167, 1.000000" />
                  <
Offset value="0.002865, -0.618056, 0.000000" />
                  <
Rotate value="0.000000, 0.000000, 0.000000" />
                  <
Alpha value="1.000000" />
                </
Properties>
              </
NavigationButton>
              <
SceneButton value="Scene1Button" >
                <
MenuStartTime value="0.000000" />
                <
MenuEndTime value="15000.000000" />
                <
InputStartOffset value="500.000000" />
                <
Properties >
                  <
Scale  value="0.206304, 0.281250, 1.000000" />
                  <
Offset value="-0.434575, 0.416667, 0.000000" />
                  <
Rotate value="0.000000, 0.000000, 0.000000" />
                  <
Alpha value="0.500000" />
                </
Properties>
              </
SceneButton>
              <
SceneButton value="Scene2Button" >
                <
MenuStartTime value="0.000000" />
                <
MenuEndTime value="15000.000000" />
                <
InputStartOffset value="500.000000" />
                <
Properties >
                  <
Scale  value="0.206304, 0.281250, 1.000000" />
                  <
Offset value="-0.000955, 0.416667, 0.000000" />
                  <
Rotate value="0.000000, 0.000000, 0.000000" />
                  <
Alpha value="1.000000" />
                </
Properties>
              </
SceneButton>
              <
SceneButton value="Scene3Button" >
                <
MenuStartTime value="0.000000" />
                <
MenuEndTime value="15000.000000" />
                <
InputStartOffset value="500.000000" />
                <
Properties >
                  <
Scale  value="0.206304, 0.281250, 1.000000" />
                  <
Offset value="0.432665, 0.416667, 0.000000" />
                  <
Rotate value="0.000000, 0.000000, 0.000000" />
                  <
Alpha value="1.000000" />
                </
Properties>
              </
SceneButton>
              <
SceneButton value="Scene4Button" >
                <
MenuStartTime value="0.000000" />
                <
MenuEndTime value="15000.000000" />
                <
InputStartOffset value="500.000000" />
                <
Properties >
                  <
Scale  value="0.206304, 0.281250, 1.000000" />
                  <
Offset value="-0.434575, -0.190972, 0.000000" />
                  <
Rotate value="0.000000, 0.000000, 0.000000" />
                  <
Alpha value="1.000000" />
                </
Properties>
              </
SceneButton>
              <
SceneButton value="Scene5Button" >
                <
MenuStartTime value="0.000000" />
                <
MenuEndTime value="15000.000000" />
                <
InputStartOffset value="500.000000" />
                <
Properties >
                  <
Scale  value="0.206304, 0.281250, 1.000000" />
                  <
Offset value="-0.000955, -0.190972, 0.000000" />
                  <
Rotate value="0.000000, 0.000000, 0.000000" />
                  <
Alpha value="1.000000" />
                </
Properties>
              </
SceneButton>
              <
SceneButton value="Scene6Button" >
                <
MenuStartTime value="0.000000" />
                <
MenuEndTime value="15000.000000" />
                <
InputStartOffset value="500.000000" />
                <
Properties >
                  <
Scale  value="0.206304, 0.281250, 1.000000" />
                  <
Offset value="0.432665, -0.190972, 0.000000" />
                  <
Rotate value="0.000000, 0.000000, 0.000000" />
                  <
Alpha value="1.000000" />
                </
Properties>
              </
SceneButton>
            </
Graph>
            <
Subpicture >
              <
Token value="Pipeline\SolidColor" >
                <
Properties >
                  <
Color value="16777215" />
                </
Properties>
              </
Token>
              <
NavigationButton value="NextMenuButton" >
                <
MenuStartTime value="0.000000" />
                <
MenuEndTime value="15000.000000" />
                <
Textures>
                  <
Source value="DvdStyles\Sample\NavigationRight_SelectionSubpicture.png" />
                </
Textures>
                <
Properties >
                  <
Scale  value="0.057307, 0.104167, 1.000000" />
                  <
Offset value="0.121299, -0.618056, 0.000000" />
                  <
Rotate value="0.000000, 0.000000, 0.000000" />
                  <
Alpha value="1.000000" />
                </
Properties>
              </
NavigationButton>
              <
NavigationButton value="ParentMenuButton" >
                <
MenuStartTime value="0.000000" />
                <
MenuEndTime value="15000.000000" />
                <
Textures>
                  <
Source value="DvdStyles\Sample\NavigationUp_SelectionSubpicture.png" />
                </
Textures>
                <
Properties >
                  <
Scale  value="0.057307, 0.104167, 1.000000" />
                  <
Offset value="-0.115568, -0.618056, 0.000000" />
                  <
Rotate value="0.000000, 0.000000, 0.000000" />
                  <
Alpha value="1.000000" />
                </
Properties>
              </
NavigationButton>
              <
NavigationButton value="PreviousMenuButton" >
                <
MenuStartTime value="0.000000" />
                <
MenuEndTime value="15000.000000" />
                <
Textures>
                  <
Source value="DvdStyles\Sample\NavigationLeft_SelectionSubpicture.png" />
                </
Textures>
                <
Properties >
                  <
Scale  value="0.057307, 0.104167, 1.000000" />
                  <
Offset value="0.002865, -0.618056, 0.000000" />
                  <
Rotate value="0.000000, 0.000000, 0.000000" />
                  <
Alpha value="1.000000" />
                </
Properties>
              </
NavigationButton>
              <
SceneButton value="Scene1Button" >
                <
MenuStartTime value="0.000000" />
                <
MenuEndTime value="15000.000000" />
                <
InputStartOffset value="500.000000" />
                <
Properties >
                  <
ButtonSelection value="TRUE" />
                  <
Scale  value="0.206304, 0.281250, 1.000000" />
                  <
Offset value="-0.434575, 0.416667, 0.000000" />
                  <
Rotate value="0.000000, 0.000000, 0.000000" />
                  <
Alpha value="1.000000" />
                </
Properties>
              </
SceneButton>
              <
SceneButton value="Scene2Button" >
                <
MenuStartTime value="0.000000" />
                <
MenuEndTime value="15000.000000" />
                <
InputStartOffset value="500.000000" />
                <
Properties >
                  <
ButtonSelection value="TRUE" />
                  <
Scale  value="0.206304, 0.281250, 1.000000" />
                  <
Offset value="-0.000955, 0.416667, 0.000000" />
                  <
Rotate value="0.000000, 0.000000, 0.000000" />
                  <
Alpha value="1.000000" />
                </
Properties>
              </
SceneButton>
              <
SceneButton value="Scene3Button" >
                <
MenuStartTime value="0.000000" />
                <
MenuEndTime value="15000.000000" />
                <
InputStartOffset value="500.000000" />
                <
Properties >
                  <
ButtonSelection value="TRUE" />
                  <
Scale  value="0.206304, 0.281250, 1.000000" />
                  <
Offset value="0.432665, 0.416667, 0.000000" />
                  <
Rotate value="0.000000, 0.000000, 0.000000" />
                  <
Alpha value="1.000000" />
                </
Properties>
              </
SceneButton>
              <
SceneButton value="Scene4Button" >
                <
MenuStartTime value="0.000000" />
                <
MenuEndTime value="15000.000000" />
                <
InputStartOffset value="500.000000" />
                <
Properties >
                  <
ButtonSelection value="TRUE" />
                  <
Scale  value="0.206304, 0.281250, 1.000000" />
                  <
Offset value="-0.434575, -0.190972, 0.000000" />
                  <
Rotate value="0.000000, 0.000000, 0.000000" />
                  <
Alpha value="1.000000" />
                </
Properties>
              </
SceneButton>
              <
SceneButton value="Scene5Button" >
                <
MenuStartTime value="0.000000" />
                <
MenuEndTime value="15000.000000" />
                <
InputStartOffset value="500.000000" />
                <
Properties >
                  <
ButtonSelection value="TRUE" />
                  <
Scale  value="0.206304, 0.281250, 1.000000" />
                  <
Offset value="-0.000955, -0.190972, 0.000000" />
                  <
Rotate value="0.000000, 0.000000, 0.000000" />
                  <
Alpha value="1.000000" />
                </
Properties>
              </
SceneButton>
              <
SceneButton value="Scene6Button" >
                <
MenuStartTime value="0.000000" />
                <
MenuEndTime value="15000.000000" />
                <
InputStartOffset value="500.000000" />
                <
Properties >
                  <
ButtonSelection value="TRUE" />
                  <
Scale  value="0.206304, 0.281250, 1.000000" />
                  <
Offset value="0.432665, -0.190972, 0.000000" />
                  <
Rotate value="0.000000, 0.000000, 0.000000" />
                  <
Alpha value="1.000000" />
                </
Properties>
              </
SceneButton>
            </
Subpicture>
          </
ScenesMenu6>
          <
ToMainTransition >
            <
Duration value="5000" />
            <
Graph >
              <
Source value="DvdStyles\Sample\BlackRectangle.bmp" />
              <
Input value="Background" >
                <
MenuStartTime value="0.000000" />
                <
MenuEndTime value="5000.000000" />
              </
Input>
              <
Token value="TFX\VideoToFill" >
                <
MenuStartTime value="0.000000" />
                <
MenuEndTime value="5000.000000" />
                <
Properties >
                  <
Scale  value="1.000000, 1.000000, 1.000000" />
                  <
Offset value="0.000000, 0.000000, 0.000000" />
                  <
Rotate value="0.000000, 0.000000, 0.000000" />
                  <
Alpha value="1.000000" />
                </
Properties>
              </
Token>
              <
Input value="InsetVideo" >
                <
MenuStartTime value="4500.000000" />
                <
MenuEndTime value="5000.000000" />
              </
Input>
              <
Token value="TFX\VideoToFill" >
                <
MenuStartTime value="4500.000000" />
                <
MenuEndTime value="5000.000000" />
                <
Properties >
                  <
Scale  value="1.000000, 1.000000, 1.000000" />
                  <
Offset value="0.000000, 0.000000, 0.000000" />
                  <
Rotate value="0.000000, 0.000000, 0.000000" />
                  <
Alpha type="float" evaluation="Linear" >
                    <
Point time="0.000000" value="0.000000" />
                    <
Point time="0.033333" value="0.000000" />
                    <
Point time="0.966667" value="1.000000" />
                    <
Point time="1.000000" value="1.000000" />
                  </
Alpha>
                </
Properties>
              </
Token>
              <
Text value="Title" >
                <
MenuStartTime value="3000.000000" />
                <
MenuEndTime value="5000.000000" />
                <
Properties >
                  <
FontSize value="18" />
                  <
ResizingTechnique value="AutoResize" />
                  <
MinAutoFontSize value="12" />
                  <
BoundingRect value="0.202674, 0.095920, 0.593696, 0.096354" />
                  <
HorizontalAlignment value="Left" />
                  <
EntranceEffect value="EffectFade" evaluation="Linear" />
                  <
EntranceDuration value="1.033333" />
                  <
EntrancePosition value="0.500000 0.500000" evaluation="Linear" />
                  <
MainPosition value="0.5 0.5" />
                </
Properties>
              </
Text>
              <
ButtonText value="PlayButton" >
                <
MenuStartTime value="4000.000000" />
                <
MenuEndTime value="5000.000000" />
                <
Properties >
                  <
FontSize value="10" />
                  <
BoundingRect value="0.622732, 0.754340, 0.171920, 0.043403" />
                  <
HorizontalAlignment value="Left" />
                  <
EntranceEffect value="EffectFade" evaluation="Linear" />
                  <
EntranceDuration value="0.333333" />
                  <
EntrancePosition value="0.500000 0.500000" evaluation="Linear" />
                  <
MainPosition value="0.5 0.5" />
                </
Properties>
              </
ButtonText>
              <
ButtonText value="Submenu1Button" >
                <
MenuStartTime value="4000.000000" />
                <
MenuEndTime value="5000.000000" />
                <
Properties >
                  <
FontSize value="10" />
                  <
BoundingRect value="0.622732, 0.806424, 0.171920, 0.043403" />
                  <
HorizontalAlignment value="Left" />
                  <
EntranceEffect value="EffectFade" evaluation="Linear" />
                  <
EntranceDuration value="0.300000" />
                  <
EntrancePosition value="0.500000 0.500000" evaluation="Linear" />
                  <
MainPosition value="0.5 0.5" />
                </
Properties>
              </
ButtonText>
              <
ButtonText value="Submenu2Button" >
                <
MenuStartTime value="4000.000000" />
                <
MenuEndTime value="5000.000000" />
                <
Properties >
                  <
FontSize value="10" />
                  <
BoundingRect value="0.622732, 0.858507, 0.171920, 0.043403" />
                  <
HorizontalAlignment value="Left" />
                  <
EntranceEffect value="EffectFade" evaluation="Linear" />
                  <
EntranceDuration value="0.316667" />
                  <
EntrancePosition value="0.500000 0.500000" evaluation="Linear" />
                  <
MainPosition value="0.5 0.5" />
                </
Properties>
              </
ButtonText>
            </
Graph>
          </
ToMainTransition>
        </
Menus>
      </
DVDMenuStyle>
    </
DVDMenuStyleDLL>
  </
DVDMenuStyles>
</
TransitionsAndEffects>

```



## Related topics

<dl> <dt>

[**Windows DVD Maker XML Extensibility**](windows-dvd-maker-xml-extensibility.md)
</dt> </dl>

 

 




