---
title: Theme File Format
description: This document discusses the format of Theme (.theme) files. A .theme file is a .ini text file that is divided into sections, which specify visual elements that appear on a Windows desktop. Section names are wrapped in brackets (\ \ ) in the .ini file.
ms.assetid: 0b7b0ff7-f55a-4215-a2fd-6c3ea117d6e8
ms.topic: article
ms.date: 05/31/2018
---

# Theme File Format

This document discusses the format of Theme (.theme) files. A .theme file is a .ini text file that is divided into sections, which specify visual elements that appear on a Windows desktop. Section names are wrapped in brackets (\[\]) in the .ini file.

A new file format, .themepack, was introduced with Windows 7 to help users share themes. Themes can be selected in the Personalization Control Panel only in Windows 7 Home Premium or higher, or only on Windows Server 2008 R2 when the Desktop component is installed.

The following topics are discussed in this article.

-   [Creating a Theme File](#creating-a-theme-file)
-   [Description of a Theme File](#description-of-a-theme-file)
    -   [\[Theme\] Section](#theme-file-format)
    -   [\[Control Panel\\Colors\] Section](#control-panelcolors-section)
    -   [\[Control Panel\\Cursors\] Section](#control-panelcursors-section)
    -   [\[Control Panel\\Desktop\] Section](#control-paneldesktop-section)
    -   [\[Slideshow\] Section](#slideshow-section)
    -   [\[Metrics\] Section](#metrics-section)
    -   [\[Visual Styles\] Section](#visual-styles-section)
    -   [\[Sounds\] and \[AppEvents\] Sections (Sounds)](#sounds-and-appevents-sections-sounds)
    -   [\[Boot\] Section](#boot-section)
    -   [\[MasterThemeSelector\] Section](#masterthemeselector-section)
-   [Example of a Theme File](#example-of-a-theme-file)
-   [Installing Theme Files](#installing-theme-files)
-   [Theme Packs](#theme-packs)
-   [Related topics](#related-topics)

## Creating a Theme File

A .theme file enables you to change the appearance of certain desktop elements. You can create or modify a .theme file in two ways:

-   Modify personalization or display settings in Control Panel and save the settings as a .theme file. See your Windows Help for instructions.
-   Create a .theme file manually for a greater level of control over the details of your theme.

To make your theme available to other users, you must supply your .theme file, as well as the background picture, screen saver, and icons files. You can do this with a [theme pack](#theme-packs).

## Description of a Theme File

Theme files have a number of required and optional sections. The following describe the sections of .theme files and provide examples of how to specify changes for the different elements.

### \[Theme\] Section

> [!Note]  
> This section is optional. If you do not include this section in your .theme file, the system uses default settings.

 

The \[Theme\] section identifies the name of your custom theme and specifies your theme's brand logo and desktop icons.

The first part of the \[Theme\] section contains the following two elements:



| Element                                                                                                                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|----------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DisplayName=name<br/> or<br/> DisplayName=@module,-stringId<br/> example: DisplayName=@themeui.dll,-2013 | DisplayName is the theme name that will show up in the Personalization Control Panel. It can be a string or a reference to a localized name.<br/> This field is optional. If it is missing, the theme filename is used as the theme name.<br/>                                                                                                                                                                                                                                         |
| BrandImage=path to image<br/> example: BrandImage=c:\\Fabrikam\\brand.png<br/>                                 | **Windows 7 and later**BrandImage specifies the path to a branded graphic file that is incorporated in the theme preview in the Personalization Control Panel.<br/> The icon graphic must be a PNG file. The graphic is scaled to 80x240 pixels, so it is recommended that you provide an image of that size. The Theme gallery respects the transparent regions of your brand icon.<br/> This field is optional. If it is missing, no logo is displayed as the theme icon.<br/> |



 

The rest of the \[Theme\] section specifies custom icons for desktop features like Computer, My Documents, Network, and Recycle Bin. If you do not specify custom desktop icons, the desktop displays the system default desktop icons.

The following are two examples of how a .theme file sets the **Computer** icon.


```
[CLSID\{20D04FE0-3AEA-1069-A2D8-08002B30309D}\DefaultIcon]
DefaultValue=%ProgramFiles%\Fabrikam\Computer.ico
```




```
; Computer
[CLSID\{20D04FE0-3AEA-1069-A2D8-08002B30309D}\DefaultIcon]
DefaultValue=%ProgramFiles%\Fabrikam\MyApp.exe,0
```



The following are values for the default desktop icons in Windows 7.


```
; Computer
[CLSID\{20D04FE0-3AEA-1069-A2D8-08002B30309D}\DefaultIcon]
DefaultValue=%SystemRoot%\System32\imageres.dll,-109

; Documents
[CLSID\{59031A47-3F72-44A7-89C5-5595FE6B30EE}\DefaultIcon]
DefaultValue=%SystemRoot%\System32\shell32.dll,-235

; Network
[CLSID\{F02C1A0D-BE21-4350-88B0-7367FC96EF3C}\DefaultIcon]
DefaultValue=%SystemRoot%\System32\imageres.dll,-25

; Recycle Bin
[CLSID\{645FF040-5081-101B-9F08-00AA002F954E}\DefaultIcon]
Full=%SystemRoot%\System32\imageres.dll,-54
Empty=%SystemRoot%\System32\imageres.dll,-55
```



### \[Control Panel\\Colors\] Section

> [!Note]  
> This section is optional. If you do not include this section in your .theme file, the system uses default settings. If your theme uses the Aero visual style, you should avoid overriding the default values in this section.

 

The color of elements, such as scroll bars, text, and buttons, are customizable. The .theme file specifies the RGB values to change for these elements. The values override the default values of the visual style and are used when your theme is based on Windows Classic, Windows 7 Basic, or High Contrast themes.

Following is an example of how colors are set.


```
[Control Panel\Colors]
ActiveTitle=10 36 106
Background=166 202 240
Hilight=10 36 106
HilightText=255 255 255
TitleText=255 255 255
Window=255 255 255
WindowText=0 0 0
Scrollbar=212 208 200
InactiveTitle=128 128 128
Menu=212 208 200
WindowFrame=0 0 0
MenuText=0 0 0
ActiveBorder=212 208 200
InactiveBorder=212 208 200
AppWorkspace=128 128 128
ButtonFace=212 208 200
ButtonShadow=128 128 128
GrayText=128 128 128
ButtonText=0 0 0
InactiveTitleText=212 208 200
ButtonHilight=255 255 255
ButtonDkShadow=64 64 64
ButtonLight=212 208 200
InfoText=0 0 0
InfoWindow=255 255 225
GradientActiveTitle=166 202 240
GradientInactiveTitle=192 192 192
```



### \[Control Panel\\Cursors\] Section

> [!Note]  
> This section is optional. If you do not include this section in your .theme file, the system uses default cursors.

 

A theme can also change the appearance of cursors. To do so, you create .cur files to replace the default Windows cursors. The following example is from a .theme file that defines the cursors for a theme called *Sports*.


```
[Control Panel\Cursors]
Arrow=%SystemRoot%\sports_arrow.cur
Help=%SystemRoot%\sports_help.cur
AppStarting=%SystemRoot%\sports_wait.ani
Wait=%SystemRoot%\sports_busy.ani
NWPen=%SystemRoot%\sports_pen.cur
No=%SystemRoot%\sports_no.cur
SizeNS=%SystemRoot%\sports_size_ns.cur
SizeWE=%SystemRoot%\sports_size_we.cur
Crosshair=%SystemRoot%\sports_cross.cur
IBeam=%SystemRoot%\sports_beam.cur
SizeNWSE=%SystemRoot%\sports_size_nwse.cur
SizeNESW=%SystemRoot%\sports_size_nesw.cur
SizeAll=%SystemRoot%\sports_move.cur
UpArrow=%SystemRoot%\sports_up.cur
DefaultValue=Windows default
```



### \[Control Panel\\Desktop\] Section

> [!Note]  
> This section is required. If you do not include this section in your .theme file, the system ignores your Theme and does not display the Theme in Control Panel.

 

You can create a custom desktop background and specify a path to the image file. The following example shows how to modify the desktop appearance.


```
[Control Panel\Desktop]
Wallpaper=%WinDir%\web\wallpaper\Windows\img0.jpg
; The path to the wallpaper picture can point to a 
; .bmp, .gif, .jpg, .png, or .tif file.

TileWallpaper=0
; 0: The wallpaper picture should not be tiled 
; 1: The wallpaper picture should be tiled 

WallpaperStyle=2
; 0:  The image is centered if TileWallpaper=0 or tiled if TileWallpaper=1
; 2:  The image is stretched to fill the screen
; 6:  The image is resized to fit the screen while maintaining the aspect 
      ratio. (Windows 7 and later)
; 10: The image is resized and cropped to fill the screen while maintaining 
      the aspect ratio. (Windows 7 and later)
```



### \[Slideshow\] Section

**Windows 7 and later.**

> [!Note]  
> This section is optional. If you do not include this section in your .theme file, the system uses the desktop background image specified in the \[Control Panel\\Desktop\] section. If you include this section, you must specify slide show settings here.

 

Your theme's background can be a slide show either of images stored locally or of images served by an RSS feed. The \[Slideshow\] section of the file contains the following attributes:



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Attribute</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Interval=number of milliseconds</td>
<td>Required. Interval is a number that determines how often the background changes. It is measured in milliseconds.</td>
</tr>
<tr class="even">
<td>Shuffle=0 or 1</td>
<td>Required. Shuffle identifies whether the background shuffles.<br/> 0 = Disabled<br/> 1 = Enabled<br/></td>
</tr>
<tr class="odd">
<td>RSSFeed=URL to RSS feed</td>
<td>Required if ImagesRootPath is not specified. RSSFeed specifies an RSS feed to use as the background slide show. For the feed to work, you need to reference high-resolution images adhering to the &quot;enclosures&quot; standard used by the <a href="/previous-versions/windows/desktop/ms684701(v=vs.85)">Windows RSS Platform</a>. Because of this limitation, .theme files that include an RSS feed must be created manually. <br/>
<blockquote>
[!Note]<br />
You cannot specify both an RSSFeed and ImagesRootPath.
</blockquote>
<br/> <br/></td>
</tr>
<tr class="even">
<td>ImagesRootPath=path to image folder</td>
<td>Required if RSSFeed is not specified. ImagesRootPath specifies a path to a set of images you want to use as the background slide show. Images in subfolders are not included in the slide show.<br/> ImagesRootPath supports Environment Variable substitutions in the path.<br/>
<blockquote>
[!Note]<br />
You cannot specify both an RSSFeed and ImagesRootPath.
</blockquote>
<br/> <br/></td>
</tr>
<tr class="odd">
<td>Item<em>N</em>Path=path(s) to specific image(s)</td>
<td>For use with ImagesRootPath. <br/> Item<em>N</em>Path specifies paths to specific images, so that you can limit the slide show to particular images instead of all images in a folder. If no paths are specified, all images in the ImagesRootPath path are used in the slide show, including images added after creating and installing the theme.<br/> Item<em>N</em>Path supports Environment Variable substitutions in the path. <em>N</em> is 0, 1, 2, and so on. <br/></td>
</tr>
</tbody>
</table>



 

The following examples show how a .theme file specifies the slide show to include a set of images stored locally.


```
[Slideshow]
Interval=1800000
Shuffle=1
ImagesRootPath=%SystemRoot%\Web\Wallpaper
```




```
[Slideshow]
Interval=1800000
Shuffle=1
ImagesRootPath=%ProgramFiles%\fabrikam\wallpaper
Item0Path=%ProgramFiles%\fabrikam\wallpaper\ocean.jpg
Item1Path=%ProgramFiles%\fabrikam\wallpaper\mountain.jpg
Item2Path=%ProgramFiles%\fabrikam\wallpaper\river.jpg
```



The following example is a template for a .theme file that creates a desktop background slide show using images from an RSS feed. Follow these steps to customize the template:

1.  Copy the following example and paste it into a text editor.
2.  Replace {themename} with the name you want to appear in the Personalization Control Panel themes gallery.
3.  Replace {rssfeedurl} with the full path to a compatible RSS feed.
4.  Save the changes as a file with the ".theme" extension.


```
[Theme]
DisplayName={themename}

[Slideshow]
Interval=1800000
Shuffle=1
RssFeed={rssfeedurl}

[Control Panel\Desktop]
TileWallpaper=0
WallpaperStyle=10
Pattern=

[Control Panel\Cursors]
AppStarting=%SystemRoot%\cursors\aero_working.ani
Arrow=%SystemRoot%\cursors\aero_arrow.cur
Crosshair=
Hand=%SystemRoot%\cursors\aero_link.cur
Help=%SystemRoot%\cursors\aero_helpsel.cur
IBeam=
No=%SystemRoot%\cursors\aero_unavail.cur
NWPen=%SystemRoot%\cursors\aero_pen.cur
SizeAll=%SystemRoot%\cursors\aero_move.cur
SizeNESW=%SystemRoot%\cursors\aero_nesw.cur
SizeNS=%SystemRoot%\cursors\aero_ns.cur
SizeNWSE=%SystemRoot%\cursors\aero_nwse.cur
SizeWE=%SystemRoot%\cursors\aero_ew.cur
UpArrow=%SystemRoot%\cursors\aero_up.cur
Wait=%SystemRoot%\cursors\aero_busy.ani
DefaultValue=Windows Aero
Link=

[VisualStyles]
Path=%SystemRoot%\resources\themes\Aero\Aero.msstyles
ColorStyle=NormalColor
Size=NormalSize
ColorizationColor=0X6B74B8FC
Transparency=1

[MasterThemeSelector]
MTSM=DABJDKT
```



### \[Metrics\] Section

> [!Note]  
> This section is optional. If you do not include this section in your .theme file, the system uses default visual style settings.

 

You can specify system metrics in a .theme file. System metrics are the dimensions of various display elements, such as the window border width, icon height, or scroll bar width. The NonclientMetrics and IconMetrics values are binary structures defined by NONCLIENTMETRICS and ICONMETRICS in winuser.h. Following is an example of how to change system metrics.


```
[Control Panel\Desktop\WindowMetrics]

[Metrics]
IconMetrics=76 0 0 0 139 0 0 0 139 0 0 0 1 0 0 0 245
255 255 255 0 0 0 0 0 0 0 0 0 0 0 0 144 1 0 0 0 0 0 0
0 0 0 0 84 97 104 111 109 97 0 119 0 0 7 0 0 0 0 0 216
31 7 0 28 52 1 1 216 31 7 0 176 36 1 1 
NonclientMetrics=84 1 0 0 1 0 0 0 16 0 0 0 16 0 0 0 18
0 0 0 18 0 0 0 245 255 255 255 0 0 0 0 0 0 0 0 0 0 0 0
188 2 0 0 0 0 0 0 0 0 0 0 84 97 104 111 109 97 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 12 0 0 0
15 0 0 0 245 255 255 255 0 0 0 0 0 0 0 0 0 0 0 0 188 2
0 0 0 0 0 0 0 0 0 0 84 97 104 111 109 97 0 0 80 37 11
0 0 0 0 0 140 221 6 0 227 115 247 119 2 40 11 0 7 0 0
0 18 0 0 0 18 0 0 0 245 255 255 255 0 0 0 0 0 0 0 0 0
0 0 0 144 1 0 0 0 0 0 0 0 0 0 0 84 97 104 111 109 97 0
0 0 0 0 0 60 222 6 0 50 71 252 119 120 1 7 0 76 73 252
119 8 6 7 0 245 255 255 255 0 0 0 0 0 0 0 0 0 0 0 0
144 1 0 0 0 0 0 0 0 0 0 0 84 97 104 111 109 97 0 119 0
0 7 0 120 1 7 0 120 1 7 0 40 37 11 0 120 1 7 0 120 1 7
0 245 255 255 255 0 0 0 0 0 0 0 0 0 0 0 0 144 1 0 0 0
0 0 0 0 0 0 0 84 97 104 111 109 97 0 0 92 1 0 0 136 4
0 0 40 37 1 1 0 0 7 0 184 221 6 0 46 75 232 119 
```



### \[Visual Styles\] Section

> [!Note]  
> This section is required. If you do not include this section in your .theme file, the system ignores your Theme and does not display the Theme in Control Panel.

 

You can supply specific information concerning the size and color of desktop elements in .msstyles files. The color and size sections of .theme files can be replaced by .msstyles files which enable you to modify desktop elements in more detail. These files are specified in the visual styles section of a .theme file. Following is an example of a visual styles section.


```
[VisualStyles]
Path=%ResourceDir%\Themes\Aero\Aero.msstyles
ColorStyle=NormalColor
Size=NormalSize
```



Adding a Path element to a .msstyles file is optional. If you supply a path, you should remove the metrics and color sections from the .theme file. When these sections are removed, the colors, fonts, and sizes for a theme come from the .msstyles file and match the .msstyles author's intent. Failing to remove the metric and color sections can cause Windows or applications to have drawing problems.

**Windows Vista / Windows 7:** When the path points to Aero.msstyles, you can specify the desired Glass Color, as shown in the following example.

**Windows 7:** When the path points to Aero.msstyles, you can also specify the desired Transparency value, as shown in the following example.


```
[VisualStyles]
Path=%SystemRoot%\resources\Themes\Aero\Aero.msstyles
ColorStyle=NormalColor
Size=NormalSize
ColorizationColor=0X7298844C
Transparency=1
```



If the ColorizationColor and Transparency values exactly match a system color, the Personalization Control Panel displays the system name for the color. Otherwise, the color is labeled "Custom."

The following shows a VisualStyles section for the Windows 7 Basic theme.


```
[VisualStyles]
Path=%ResourceDir%\Themes\Aero\Aero.msstyles
Composition=0
ColorStyle=NormalColor
Size=NormalSize
ColorizationColor=0x6B74B8FC
Transparency=1
```



The following shows a VisualStyles section for the Windows Classic theme.


```
[VisualStyles]
Path=
ColorStyle=@themeui.dll,-854
Size=@themeui.dll,-2019
Transparency=0
```



The following shows a VisualStyles section for a High Contrast Black theme.


```
[VisualStyles]
Path=
ColorStyle=@themeui.dll,-852
Size=@themeui.dll,-2019
Transparency=0
```



### \[Sounds\] and \[AppEvents\] Sections (Sounds)

> [!Note]  
> This section is optional. If you do not include this section in your .theme file, the system uses default sound settings.

 

The user can select the **Sound** icon in Control Panel to associate sounds with events that occur in applications. For example, a .wav file can play when an application is opened. A .theme file can specify .wav files to replace the default ones. The following example shows how to do this.


```
[AppEvents\Schemes\Apps\.Default\SystemExclamation]
DefaultValue=%WinDir%\media\chord.wav

[AppEvents\Schemes\Apps\.Default\SystemExit]
DefaultValue=%WinDir%\media\tada.wav

[AppEvents\Schemes\Apps\.Default\SystemHand]
DefaultValue=%WinDir%\media\chord.wav

[AppEvents\Schemes\Apps\.Default\SystemQuestion]
DefaultValue=%WinDir%\media\chord.wav

[AppEvents\Schemes\Apps\.Default\SystemStart]
DefaultValue=%WinDir%\media\The Microsoft Sound.wav

[AppEvents\Schemes\Apps\Explorer\EmptyRecycleBin]
DefaultValue=%WinDir%\media\ding.wav
```



**Windows 7 and later:** A sound scheme name can be specified instead of listing each sound separately.


```
[Sounds]
; "Quirky" sound scheme
SchemeName=@%SystemRoot%\System32\mmres.dll,-819
```



The SchemeName value specifies the sound scheme name or the localized sound scheme name, as shown in the example above.

### \[Boot\] Section

> [!Note]  
> **Screen Savers are deprecated in the Windows 10 Anniversary Update and beyond.**

 

> [!Note]  
> This section is optional. If you do not include this section in your .theme file, no screen saver is used.

 

In the .theme file, you can specify the screen saver for Windows to use. The following example shows this.


```
[boot]
SCRNSAVE.EXE=%WinDir%\System32\bubbles.scr
```



### \[MasterThemeSelector\] Section

> [!Note]  
> This section is required. If you do not include this section in your .theme file, the system ignores your Theme and does not display the Theme in Control Panel.

 

The master theme selector section of the .theme file should always be included as a tag that indicates the file is valid. You do not have a choice of values for this parameter. The following shows this.


```
[MasterThemeSelector]
MTSM=DABJDKT
```



## Example of a Theme File

The following example shows a complete .theme file.


```
[Theme]
DisplayName=My Current Theme
BrandImage=c:\Fabrikam\brand.png

; Computer
[CLSID\{20D04FE0-3AEA-1069-A2D8-08002B30309D}\DefaultIcon]
DefaultValue=%SystemRoot%\System32\imageres.dll,-109

; Documents
[CLSID\{59031A47-3F72-44A7-89C5-5595FE6B30EE}\DefaultIcon]
DefaultValue=%SystemRoot%\System32\shell32.dll,-235

; Network
[CLSID\{F02C1A0D-BE21-4350-88B0-7367FC96EF3C}\DefaultIcon]
DefaultValue=%SystemRoot%\System32\imageres.dll,-25

; Recycle Bin
[CLSID\{645FF040-5081-101B-9F08-00AA002F954E}\DefaultIcon]
Full=%SystemRoot%\System32\imageres.dll,-54
Empty=%SystemRoot%\System32\imageres.dll,-55

[Control Panel\Cursors]
Arrow=
Help=
AppStarting=
Wait=
NWPen=
No=
SizeNS=
SizeWE=
Crosshair=
IBeam=
SizeNWSE=
SizeNESW=
SizeAll=
UpArrow=
DefaultValue=Windows default

[Control Panel\Desktop]
Wallpaper=%ProgramFiles%\fabrikam\wallpaper\ocean.jpg
TileWallpaper=0
WallpaperStyle=2
Pattern=
ScreenSaveActive=0

[AppEvents\Schemes\Apps\.Default\.Default]
DefaultValue=%WinDir%\media\ding.wav

[AppEvents\Schemes\Apps\.Default\AppGPFault]
DefaultValue=

[AppEvents\Schemes\Apps\.Default\Maximize]
DefaultValue=

[AppEvents\Schemes\Apps\.Default\MenuCommand]
DefaultValue=

[AppEvents\Schemes\Apps\.Default\MenuPopup]
DefaultValue=

[AppEvents\Schemes\Apps\.Default\Minimize]
DefaultValue=

[AppEvents\Schemes\Apps\.Default\Open]
DefaultValue=

[AppEvents\Schemes\Apps\.Default\RestoreDown]
DefaultValue=

[AppEvents\Schemes\Apps\.Default\RestoreUp]
DefaultValue=

[AppEvents\Schemes\Apps\.Default\RingIn]
DefaultValue=

[AppEvents\Schemes\Apps\.Default\Ringout]
DefaultValue=

[AppEvents\Schemes\Apps\.Default\SystemAsterisk]
DefaultValue=%WinDir%\media\chord.wav

[AppEvents\Schemes\Apps\.Default\SystemDefault]
DefaultValue=

[AppEvents\Schemes\Apps\.Default\SystemExclamation]
DefaultValue=%WinDir%\media\chord.wav

[AppEvents\Schemes\Apps\.Default\SystemExit]
DefaultValue=

[AppEvents\Schemes\Apps\.Default\SystemHand]
DefaultValue=%WinDir%\media\chord.wav

[AppEvents\Schemes\Apps\.Default\SystemQuestion]
DefaultValue=%WinDir%\media\chord.wav

[AppEvents\Schemes\Apps\.Default\SystemStart]
DefaultValue=

[AppEvents\Schemes\Apps\Explorer\EmptyRecycleBin]
DefaultValue=%WinDir%\media\ding.wav

[AppEvents\Schemes\Apps\.Default\Close]
DefaultValue=

[Slideshow]
Interval=1800000
Shuffle=1
ImagesRootPath=%ProgramFiles%\fabrikam\wallpaper
Item0Path=%ProgramFiles%\fabrikam\wallpaper\ocean.jpg
Item1Path=%ProgramFiles%\fabrikam\wallpaper\mountain.jpg
Item2Path=%ProgramFiles%\fabrikam\wallpaper\river.jpg

[boot]
SCRNSAVE.EXE=%WinDir%\System32\bubbles.scr

[MasterThemeSelector]
MTSM=DABJDKT
ThemeColorBPP=4

[VisualStyles]
Path=%SystemRoot%\resources\Themes\Aero\Aero.msstyles
ColorStyle=NormalColor
Size=NormalSize
ColorizationColor=0x856E3BA1
Transparency=1
```



## Installing Theme Files

When Windows is initialized, the operating system enumerates the first-level subdirectories of %WinDir%\\Resources\\ to identify available themes. The system default theme files are located in %WinDir%\\Resources\\Themes. The user theme files are stored in %WinDir%\\Users\\<username>\\AppData\\Local\\Microsoft\\Windows\\Themes.

A .theme file has file associations; therefore, theme installer applications can call [**ShellExecute**](/windows/desktop/api/shellapi/nf-shellapi-shellexecutea) on a .theme file to open the **Personalization** window in Control Panel to the specified theme.

## Theme Packs

**Windows 7 and later.** A theme pack is a .cab file that contains not only the .theme file but also the files needed to implement the theme on another computer, such as sound files and images. Users can create theme packs through the Personalization Control Panel.

Supported file types include the following:

| File type    | Extension                           |
|--------------|-------------------------------------|
| Theme        | .theme                              |
| Image        | .jpg, .jpeg, .bmp, .dib, .tif, .png |
| Sound        | .wav                                |
| Mouse cursor | .cur, .ani                          |
| Desktop icon | .ico                                |
| Brand logo   | .png                                |

Assets like sounds should be placed at the root of the .cab and referenced in .theme files directly. For example, if you have a file called `Alert.wav` in the root of your .cab, you can use it in your sound scheme:

```ini
[AppEvents\Schemes\Apps\.Default\SystemAsterisk]
DefaultValue=Alert.wav
```

Wallpaper images should be handled differently. They should extract to a `DesktopBackground\` folder and be referenced in .theme files by that subdirectory. For example, if you have a wallpaper called `BestDesktop.jpg`, ensure it extracts to `DesktopBackground\`, and reference it in your .cab like this:

```
[Control Panel\Desktop]
; Note the extra `DesktopBackground\` directory.
Wallpaper=DesktopBackground\BestDesktop.jpg
```

## Related topics

<dl> <dt>

[Visual Styles Overview](visual-styles-overview.md)
</dt> </dl>

