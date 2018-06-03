---
title: Shared Samples
description: This topic contains a number of code examples that show how to accomplish various tasks.
ms.assetid: 676a2ea4-6c7b-44ec-9a5c-219127553b71
keywords:
- Windows Image Acquisition (WIA),examples
- WIA (Windows Image Acquisition),examples
- Windows Image Acquisition Automation Layer,examples
- WIA Automation Layer,examples
- Image Acquisition Automation Layer,examples
- Windows Image Acquisition (WIA),sample code
- WIA (Windows Image Acquisition),sample code
- Windows Image Acquisition Automation Layer,sample code
- WIA Automation Layer,sample code
- Image Acquisition Automation Layer,sample code
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Shared Samples

This topic contains a number of code examples that show how to accomplish various tasks. Some of them are complete code examples while others need to be inserted into a template code. See [Getting Started with Samples](-wiaaut-getting-started-samples.md) for the appropriate code template for your preferred development environment.

> [!Note]  
> The individual reference pages contain additional code examples that are not included in this topic. See also [How To Use Filters](-wiaaut-howto-use-filters.md) for filter-related sample code.

 

-   [Download New Items as They are Created](#download-new-items-as-they-are-created)
-   [Convert a File](#convert-a-file)
-   [Take a Picture](#take-a-picture)
-   [Display Detailed Property Information](#display-detailed-property-information)
-   [Determine Whether the Selected Device Is a Camera](#determine-whether-the-selected-device-is-a-camera)
-   [Count Root-Level Images for Transfer](#count-root-level-images-for-transfer)
-   [Display all ImageFile Properties](#display-all-imagefile-properties)
-   [Determine the Event Type](#determine-the-event-type)
-   [Set Rational Numerator and Denominator](#set-rational-numerator-and-denominator)
-   [Create and Initialize a Vector Object](#create-and-initialize-a-vector-object)
-   [Display Detailed Image Information](#display-detailed-image-information)
-   [Create an ImageProcess Object and Enumerate Filters](#create-an-imageprocess-object-and-enumerate-filters)
-   [Create an ImageProcess Object and Create One of Each Available Filter](#create-an-imageprocess-object-and-create-one-of-each-available-filter)
-   [List the Supported Transfer Formats](#list-the-supported-transfer-formats)
-   [Enumerate Supported Commands in Commands Collection](#enumerate-supported-commands-in-commands-collection)
-   [Enumerate Root-Level Items and Display Their Names](#enumerate-root-level-items-and-display-their-names)
-   [Determine the Number of Items Returned by ShowSelectItems](#determine-the-number-of-items-returned-by-showselectitems)
-   [Enumerate all the Supported Events for the Selected Device](#enumerate-all-the-supported-events-for-the-selected-device)
-   [List all Available Devices by Name and DeviceID](#list-all-available-devices-by-name-and-deviceid)
-   [Display all the Properties for the Selected Device - 1](#display-all-the-properties-for-the-selected-device---1)
-   [Display all the Properties for the Selected Device - 2](#display-all-the-properties-for-the-selected-device---2)
-   [Use VideoPreview Control in HTML](#use-videopreview-control-in-html)
-   [Implement a Web Camera ASP Page](#implement-a-web-camera-asp-page)
-   [Enumerate the Supported Commands](#enumerate-the-supported-commands)
-   [Create an ImageFile Object that Contains a Blank Page](#create-an-imagefile-object-that-contains-a-blank-page)
-   [Implement a Windows Script Host Script that Runs Automatically](#implement-a-windows-script-host-script-that-runs-automatically)
-   [Count the Number of Child Items Available for Transfer](#count-the-number-of-child-items-available-for-transfer)
-   [Use a Vector Object](#use-a-vector-object)

## Download New Items as They are Created

The following example is a complete sample that shows how to implement a Microsoft Visual Basic project that waits for new items to be created and then downloads them to display on a form.

To create a Visual Basic project for this example, do the following:

-   Launch the Visual Basic IDE.
-   Click Standard EXE.
-   Select Components from the Project menu (or press CTRL+T)
-   Select the **Microsoft Windows Image Acquisition Library v2.0** check box.
-   Of the three new controls that appear in the Toolbox, double-click [**CommonDialog**](-wiaaut-commondialog.md) and DeviceManager to add them to your form.
-   Double-click the PictureBox control to add it to your form.
-   Position the PictureBox control in the upper left-hand corner of the form and change its AutoSize property to True.
-   Copy and paste the following code into the form's code view.


```
Private Sub Form_Load()
    DeviceManager1.RegisterEvent wiaEventItemCreated, wiaAnyDeviceID
End Sub

Private Sub DeviceManager1_OnEvent(ByVal EventID As String, ByVal DeviceID As String, ByVal ItemID As String)
    Dim dev As Device
    Dim itm As Item
    Dim img As ImageFile
    Dim v As Vector

    Set dev = DeviceManager1.DeviceInfos(DeviceID).Connect
    Set itm = dev.GetItem(ItemID)
    Set img = CommonDialog1.ShowTransfer(itm)
    Set v = img.FileData
    Set Picture1.Picture = v.Picture
End Sub
```



## Convert a File

The following example shows how to convert a file returned by [**ShowAcquireImage**](-wiaaut-icommondialog-showacquireimage.md) to a JPEG file, if it is not one already.


```
Dim Img 'As ImageFile

Set Img = CommonDialog1.ShowAcquireImage

If Img.FormatID <> wiaFormatJPEG Then
    Dim IP 'As New ImageProcess
    Set IP = CreateObject( "Wia.ImageProcess" )
    
    IP.Filters.Add IP.FilterInfos("Convert").FilterID
    IP.Filters(1).Properties("FormatID").Value = wiaFormatJPEG
    Set Img = IP.Apply(Img)
End If
```



## Take a Picture

The following example shows how to signal a camera to take a picture if the device selected is a camera.


```
Dim dev 'As Device

Set dev = CommonDialog1.ShowSelectDevice

If dev.Type = CameraDeviceType Then
    Dim itm 'As Item

    Set itm = dev.ExecuteCommand(wiaCommandTakePicture)
End If
```



## Display Detailed Property Information

The following example shows how to display detailed information about all the properties on the selected device.


```
Dim dev 'As Device
Dim p 'As Property
Dim s 'As String
Dim i 'As Integer

Set dev = CommonDialog1.ShowSelectDevice

For Each p In dev.Properties
    s = p.Name & "(" & p.PropertyID & ") = "
    If p.IsVector Then
        s = s & "[vector of data]"
    Else
        s = s & p.Value
        If p.SubType <> UnspecifiedSubType Then       
            If p.Value <> p.SubTypeDefault Then
                s = s & "(Default = " & p.SubTypeDefault & ")"
            End If
        End If
    End If

    If p.IsReadOnly then
        s= s & " [READ ONLY]"
    else
        Select Case p.SubType
        Case FlagSubType
            s = s & " [ valid flags include:"
            For i = 1 To p.SubTypeValues.Count
                s = s & p.SubTypeValues(i)
                If i <> p.SubTypeValues.Count Then
                    s = s & ", "
                End If
            Next
            s = s & " ]"
        Case ListSubType
            s = s & " [ valid values include:"
            For i = 1 To p.SubTypeValues.Count
                s = s & p.SubTypeValues(i)
                If i <> p.SubTypeValues.Count Then
                    s = s & ", "
                End If
            Next
            s = s & " ]"
        Case RangeSubType
            s = s & " [ valid values in the range from " & _
                   p.SubTypeMin & " to " & p.SubTypeMax & _
                   " in increments of " & p.SubTypeStep & " ]"
        Case Else 'UnspecifiedSubType
        End Select
    End If

    MsgBox s
Next
```



## Determine Whether the Selected Device Is a Camera

The following example shows how to determine if the selected device is a camera.


```
Dim dev 'As Device

Set dev = CommonDialog1.ShowSelectDevice

If dev.Type = CameraDeviceType Then
    MsgBox "Selected device is a camera"
End If
```



## Count Root-Level Images for Transfer

The following example shows how to count the number of root-level image items available for transfer on the selected device.


```
Dim d 'As Device
Dim itm 'As Item
Dim i 'As Integer

i = 0
Set d = CommonDialog1.ShowSelectDevice
For Each itm In d.Items
    Dim f
    f = itm.Properties("Item Flags")
    If (f And ImageItemFlag) = ImageItemFlag Then
       i = i + 1
    End If
Next

MsgBox "Selected device has " & i & " top-level images"
```



## Display all ImageFile Properties

The following example shows how to display all the properties with rich formatting for the [**ImageFile**](-wiaaut-imagefile.md) returned by [**ShowAcquireImage**](-wiaaut-icommondialog-showacquireimage.md).


```
Dim Img 'As ImageFile
Dim p 'As Property

Set Img = CommonDialog1.ShowAcquireImage

For Each p In Img.Properties
    Dim s 'As String

    s = p.Name & "(" & p.PropertyID & ") = "
    If p.IsVector Then
        s = s & "[vector data not emitted]"
    ElseIf p.Type = RationalImagePropertyType Then
        s = s & p.Value.Numerator & "/" & p.Value.Denominator
    ElseIf p.Type = StringImagePropertyType Then
        s = s & """" & p.Value & """"
    Else
        s = s & p.Value
    End If

    MsgBox s
Next
```



## Determine the Event Type

The following example shows how to determine the event type for each supported event for the selected device.


```
Dim dev 'As Device
Dim e 'As DeviceEvent

Set dev = CommonDialog1.ShowSelectDevice

For Each e In dev.Events
    If (e.Type And ActionEvent) = ActionEvent Then
        MsgBox e.Name & " is an Action event"
    Else
        MsgBox e.Name & " is not an Action event"
    End If
Next
```



## Set Rational Numerator and Denominator

The following example shows how to create a [**Rational**](-wiaaut-rational.md) object and set the [**Numerator**](-wiaaut-irational-numerator.md) and [**Denominator**](-wiaaut-irational-denominator.md) properties with two different sets of values that produce the same value when reading the Value property.


```
Dim r 'As Rational

Set r = CreateObject("WIA.Rational")

r.Numerator = 1
r.Denominator = 3

MsgBox "1/3 = " & r.Value

r.Numerator = 2
r.Denominator = 6

MsgBox "2/6 = " & r.Value
```



## Create and Initialize a Vector Object

The following example shows how to create a [**Vector**](-wiaaut-vector.md) object then initialize it as a vector of Bytes containing the ASCII string "This is a test".


```
Dim v 'As Vector
Dim i 'As Integer

Set v = CreateObject("WIA.Vector")

v.SetFromString "This is a test", True, False

For i = 1 To v.Count
    MsgBox Chr(v(i))
Next
```



## Display Detailed Image Information

The following example shows how to display detailed information about one of the sample pictures from Windows XP.


```
Dim Img 'As ImageFile
Dim s 'As String
Dim v 'As Vector

set Img = CreateObject("WIA.ImageFile")

Img.LoadFile "C:\WINDOWS\Web\Wallpaper\Autumn.jpg"

s = "Width = " & Img.Width & vbCrLf & _
    "Height = " & Img.Height & vbCrLf & _
    "Depth = " & Img.PixelDepth & vbCrLf & _
    "HorizontalResolution = " & Img.HorizontalResolution & vbCrLf & _
    "VerticalResolution = " & Img.VerticalResolution & vbCrLf & _
    "FrameCount = " & Img.FrameCount & vbCrLf

If Img.IsIndexedPixelFormat then
    s = s & "Pixel data contains palette indexes" & vbCrLf
End If

If Img.IsAlphaPixelFormat then
    s = s & "Pixel data has alpha information" & vbCrLf
End If

If Img.IsExtendedPixelFormat then
    s = s & "Pixel data has extended color information (16 bit/channel)" & vbCrLf
End If

If Img.IsAnimated then
    s = s & "Image is animated" & vbCrLf
End If

If Img.Properties.Exists("40091") then
    Set v = Img.Properties("40091").Value
    s = s & "Title = " & v.String & vbCrLf
End If

If Img.Properties.Exists("40092") then
    Set v = Img.Properties("40092").Value
    s = s & "Comment = " & v.String & vbCrLf
End If

If Img.Properties.Exists("40093") then
    Set v = Img.Properties("40093").Value
    s = s & "Author = " & v.String & vbCrLf
End If

If Img.Properties.Exists("40094") then
    Set v = Img.Properties("40094").Value
    s = s & "Keywords = " & v.String & vbCrLf
End If

If Img.Properties.Exists("40095") then
    Set v = Img.Properties("40095").Value
    s = s & "Subject = " & v.String & vbCrLf
End If

MsgBox s
```



## Create an ImageProcess Object and Enumerate Filters

The following example shows how to create an [**ImageProcess**](-wiaaut-imageprocess.md) object and enumerate all the filters available in the FilterInfos collection.


```
Dim IP 'As ImageProcess
Dim fi 'As FilterInfo
Dim s 'As String

Set IP = CreateObject("WIA.ImageProcess")

For Each fi In IP.FilterInfos
    s = fi.Name & vbCrLf & _
    "==================================================" & vbCrLf & _
    fi.Description
    MsgBox s
Next
```



## Create an ImageProcess Object and Create One of Each Available Filter

The following example shows how to create an [**ImageProcess**](-wiaaut-imageprocess.md) object and then create one of each kind of filter available so as to generate detailed information about each of the properties.


```
Function StringValue(v)
    If TypeName(v) = "String" Then
        StringValue = """" & v & """"
    Else
        StringValue = v
    End If
End Function

Function ListValues(v)
    Dim i 'As Integer

    ListValues = ""
    For i = 1 To v.Count
        ListValues = ListValues & StringValue(v(i))
        If i <> v.Count Then
            ListValues = ListValues & ", "
        End If
    Next
End Function

Sub ListProperties(filter)
Dim p 'As Property
Dim s 'As String
Dim i 'As Integer

s = filter.Name & " (" & filter.FilterID & ")" & vbCrLf & _
    "==================================================" & vbCrLf & _
    filter.Description & vbCrLf & _
    "==================================================" & vbCrLf

For Each p In filter.Properties
    If Not IsObject(p.Value) Then
        s = s & "IP.Filters(1).Properties(""" & p.Name & """) = " & _
            StringValue(p.Value)

        Select Case p.SubType
        Case FlagSubType
            s = s & " '[valid values formed by using the OR operator with the following bit flags: " & _
                ListValues(p.SubTypeValues) & "]" & vbCrLf
        Case ListSubType
            s = s & " '[valid values from the following list: " & _
                ListValues(p.SubTypeValues) & "]" & vbCrLf
        Case RangeSubType
            s = s & " '[valid values in the range: Min = " & p.SubTypeMin & _
                ", Max = " & p.SubTypeMax & ", Step = " & p.SubTypeStep & "]" & _
                vbCrLf
        Case Else 'UnspecifiedSubType
            s = s & vbCrLf
        End Select
    Else
        s = s & "IP.Filters(1).Properties(""" & p.Name & """) = " & _
            TypeName(p.Value) & vbCrLf
    End If
Next

MsgBox s
End Sub

Dim IP 'As ImageProcess
Dim i 'As Integer

Set IP = CreateObject("WIA.ImageProcess")

For i = 1 to IP.FilterInfos.Count
    IP.Filters.Add IP.FilterInfos(i).FilterID
    ListProperties IP.Filters(1)
    IP.Filters.Remove 1
Next
```



## List the Supported Transfer Formats

The following example shows how to list the supported transfer formats for the selected item.


```
Function StringFormat(fid)
    Select Case fid
    Case wiaFormatBMP
        StringFormat = "BMP"
    Case wiaFormatPNG
        StringFormat = "PNG"
    Case wiaFormatGIF
        StringFormat = "GIF"
    Case wiaFormatJPEG
        StringFormat = "JPEG"
    Case wiaFormatTIFF
        StringFormat = "TIFF"
    Case Else
        StringFormat = "Unknown"
    End Select
End Function

Dim dev 'As Device
Dim itms 'As Items
Dim itm 'As Item
Dim i 'As Integer
Dim s 'As String

Set dev = CommonDialog1.ShowSelectDevice
Set itms = CommonDialog1.ShowSelectItems(dev, UnspecifiedIntent, _
                                         MaximizeQuality, True)
Set itm = itms(1)
s = ""
For i = 1 To itm.Formats.Count
    s = s & StringFormat(itm.Formats(i))
    If i <> itm.Formats.Count Then
        s = s & ", "
    End If
Next

MsgBox "Selected item can be transferred in the following formats: " & vbCrLf & s
```



## Enumerate Supported Commands in Commands Collection

The following example shows how to enumerate the supported commands in the Commands collection to see if the selected device supports the "Take Picture" command.


```
Dim dev 'As Device
Dim dc 'As DeviceCommand

Set dev = CommonDialog1.ShowSelectDevice
For Each dc In dev.Commands
    If dc.CommandID = wiaCommandTakePicture Then
        MsgBox "Selected device supports the TakePicture command"
    End If
Next
```



## Enumerate Root-Level Items and Display Their Names

The following example shows how to enumerate over all the root-level items for the selected device and display the names of the root items.


```
Dim d 'As Device
Dim itm 'As Item
Dim s 'As String

Set d = CommonDialog1.ShowSelectDevice
For Each itm In d.Items
    s = itm.Properties("Item Name").Value
    If itm.Properties.Exists("Item Time Stamp") Then
        Dim v 'As Vector

        Set v = itm.Properties("Item Time Stamp").Value
        If v.Count = 8 Then
            s = s & " (" & v.Date & ")"
        End If
    End If
    MsgBox s
Next
```



## Determine the Number of Items Returned by ShowSelectItems

The following example shows how to determine the number of items returned by ShowSelectItems.


```
Dim dev 'As Device
Dim itms 'As Items

Set dev = CommonDialog1.ShowSelectDevice
Set itms = CommonDialog1.ShowSelectItems(dev , UnspecifiedIntent, _
                                         MaximizeQuality, False)

MsgBox "You selected " & itms.Count & " item(s)"
```



## Enumerate all the Supported Events for the Selected Device

The following example shows how to enumerate all the supported events for the selected device.


```
Dim dev 'As Device
Dim i 'As Integer
Dim s 'As String

Set dev = CommonDialog1.ShowSelectDevice

s = ""
For i = 1 To dev.Events.Count
    s = s & dev.Events(i).Name & " (" & dev.Events(i).EventID & _
        "): " & dev.Events(i).Description & vbCrLf
Next

MsgBox "The selected device supports the following events:" & vbCrLf & s
```



## List all Available Devices by Name and DeviceID

The following example shows how to list all available devices by name and DeviceID.


```
Dim i 'As Integer

For i = 1 to DeviceManager1.DeviceInfos.Count
    MsgBox DeviceManager1.DeviceInfos(i).Properties("Name").Value & vbCrLf & _
           "(" & DeviceManager1.DeviceInfos(i).DeviceID & ")"
Next
```



## Display all the Properties for the Selected Device - 1

The following example shows how to display all the properties for the selected device.


```
Dim dev 'As Device
Dim p 'As Property
Dim s 'As String

Set dev = CommonDialog1.ShowSelectDevice

For Each p In dev.Properties
    s = p.Name & "(" & p.PropertyID & ") = "
    If p.IsVector Then
        s = s & "[vector of data]"
    Else
        If p.Type = StringPropertyType Then
            s = s & """" & p.Value & """"
        Else
            s = s & p.Value
        End If
    End If
    
    MsgBox s
Next
```



## Display all the Properties for the Selected Device - 2

Similar to the previous example, the following example shows how to display all the properties for the selected device using a For-to loop instead of a For-Each loop.


```
Dim dev 'As Device
Dim i 'As Integer
Dim s 'As String

Set dev = CommonDialog1.ShowSelectDevice

For i = 1 to dev.Properties.Count
    s = dev.Properties(i).Name & "(" & dev.Properties(i).PropertyID & ") = "
    If dev.Properties(i).IsVector Then
        s = s & "[vector of data]"
    Else
        If dev.Properties(i).Type = StringPropertyType Then
            s = s & """" & dev.Properties(i).Value & """"
        Else
            s = s & dev.Properties(i).Value
        End If
    End If
    
    MsgBox s
Next
```



## Use VideoPreview Control in HTML

The following example is a complete sample that shows how to implement an HTML page or HTML Application (HTA) containing a VideoPreview control.


```
<html>
<head><title>Video Sample</title></head>
<body>
<table border=1>
<tr><td>
<object id="VideoPreview"
    width=640 height=480
    classid="clsid:0B5F2CC8-5E1E-44F9-899B-3B789705AFCA">
</object></td></tr>
<tr><td align=center><input id=btnpause type=button value=pause></td></tr>
</table>

<script language="VBScript">

Sub window_OnLoad()
    If VideoPreview.Device is nothing then
        document.body.innerHTML = "Video devices Are either unavailable or in use."
    End If
End Sub

Sub btnPause_OnClick()
    If VideoPreview.Pause Then
        VideoPreview.Pause = False
        btnPause.value = "Pause"
    Else
        VideoPreview.Pause = True
        btnPause.value = "Resume"
    End If
End Sub

</script>
</body>
</html>
```



## Implement a Web Camera ASP Page

The following example is a complete sample that shows how to implement a Web camera ASP page using the Windows Image Acquisition (WIA) Library.

> [!Note]  
> In the interest of increased security, the default Server Security Settings need to be adjusted before you can successfully create a [**DeviceManager**](-wiaaut-devicemanager.md) object. See [How to Configure Security Settings](-wiaaut-configure-security.md) for information about how to configure security settings.

 


```
<%@ Language=VBScript %>
<!--METADATA TYPE="TypeLib" UUID="94A0E92D-43C0-494E-AC29-FD45948A5221"-->
<%
    Dim oImage
    Dim oDeviceManager
    Dim oDeviceInfo
    Dim oDevice
    Dim oItem
    Dim oVector

    Set oDeviceManager = Server.CreateObject("WIA.DeviceManager")

    For Each oDeviceInfo In oDeviceManager.DeviceInfos
        If oDeviceInfo.Type = VideoDeviceType Then
            Set oDevice = oDeviceInfo.Connect
            Exit For
        End If
    Next

    If oDevice Is Nothing Then
        Response.Write "There is no Video Device"
        Response.End
    End If

    Set oItem = oDevice.ExecuteCommand(wiaCommandTakePicture)

    Set oImage = oItem.Transfer
    Set oVector = oImage.FileData
    Response.BinaryWrite oVector.BinaryData
%>
```



## Enumerate the Supported Commands

The following example shows how to enumerate the supported commands on the item returned from ShowSelectItems.


```
Dim dev 'As Device
Dim itms 'As Items
Dim itm 'As Item
Dim dc 'As DeviceCommand
Dim i 'As Integer
Dim s 'As String

Set dev = CommonDialog1.ShowSelectDevice
Set itms = CommonDialog1.ShowSelectItems(dev, UnspecifiedIntent, _
                                         MaximizeQuality, True)
Set itm = itms(1)

s = ""
For i = 1 To itm.Commands.Count
    s = s & itm.Commands(i).Name & ": " & itm.Commands(i).Description & vbCrLf
Next

MsgBox "The selected item supports the following commands:" & vbCrLf & s
```



## Create an ImageFile Object that Contains a Blank Page

The following example shows how to create an [**ImageFile**](-wiaaut-imagefile.md) object that contains a blank image.


```
Dim v 'As Vector
Dim Img 'As ImageFile
Dim c 'As Long

c = &amp;hFF0000FF 'opaque blue (A=255,R=0,G=0,B=255)
Set v = CreateObject("WIA.Vector")

v.Add c
v.Add c
v.Add c
v.Add c

Set Img = v.ImageFile(2, 2)

Img.SaveFile "C:\WINDOWS\Web\Wallpaper\Blue." & Img.FileExtension
```



## Implement a Windows Script Host Script that Runs Automatically

The following example is a complete sample that shows how to implement a Windows Script Host (.wsf) script that can register itself to automatically run when an imaging device is connected and download all the top-level items to the C:\\Windows\\Web\\Wallpaper directory. Then, (if you remove the comments from the code below) the sample removes the picture from the camera.


```
<job>
<reference object="wia.DeviceManager" />
<object id="DevMan" progid="Wia.DeviceManager" />
<script language="VBScript">
Option Explicit

Dim Command, Name, Description, Icon, EventID, DeviceID, i

Command = WScript.fullname & " """ & WScript.scriptfullname & """ connect"
Name = "QuickTransfer"
Description = "Quick Scripting Transfer"
Icon = WScript.fullname & ", 0"
EventID = wiaEventDeviceConnected
DeviceID = "*"

If WScript.arguments.count = 1 then
    If UCase(WScript.arguments(0)) = "REGISTER" then
        MsgBox "Registering Event Handler"
        DevMan.RegisterPersistentEvent Command, Name, Description, Icon, EventID, DeviceID
        WScript.quit
    End If
    If UCase(WScript.arguments(0)) = "UNREGISTER" then
        MsgBox "Unregistering Event Handler"
        DevMan.UnregisterPersistentEvent Command, Name, Description, Icon, EventID, DeviceID
        WScript.quit
    End If
End If

If WScript.arguments.count = 2 then
    If UCase(WScript.arguments(0)) = "REGISTER" then
        MsgBox "Registering Event Handler"
        DeviceID = WScript.arguments(1)
        DevMan.RegisterPersistentEvent Command, Name, Description, Icon, EventID, DeviceID
        WScript.quit
    End If
    If UCase(WScript.arguments(0)) = "UNREGISTER" then
        MsgBox "Unregistering Event Handler"
        DeviceID = WScript.arguments(1)
        DevMan.UnregisterPersistentEvent Command, Name, Description, Icon, EventID, DeviceID
        WScript.quit
    End If
End If

If WScript.arguments.count = 3 Then
    If UCase(WScript.arguments(0)) = "CONNECT" Then
        Dim DevID
        Dim Dev
        Dim Itm
        Dim Img

        DevID = Mid(WScript.arguments(1), 12)
        set Dev = DevMan.DeviceInfos(DevID).Connect

        For Each Itm in Dev.Items
            Set Img = Itm.Transfer
            Img.SaveFile "C:\Windows\Web\Wallpaper\" & Itm.Properties("Item Name").Value & "." & Img.FileExtension

            'Uncomment the following lines to remove the picture from the
            'Camera after transfer

            'For i = 1 to Dev.Items.Count
            '   If Dev.Items(i).ItemID = itm.ItemID Then
            '       'Some Cameras don't support deleting pictures
            '       On Error Resume Next
            '       Dev.Items.Remove i
            '       If Err.Number <> 0 Then
            '           MsgBox Err.Description
            '           Err.Clear
            '       End If
            '       On Error Goto 0
            '       Exit For
            '   End If
            'Next
        Next
        WScript.quit
    End If
End If

Description = "Usage:" & vbCrLf & vbCrLf & "To register type:" & vbCrLf & vbCrLf & _
                WScript.ScriptName & " register" & vbCrLf & "...or..." & vbCrLf & _
                WScript.ScriptName & " register DeviceID" & vbCrLf  & vbCrLf & _
                "To unregister type:" & vbCrLf  & vbCrLf & WScript.ScriptName & _
                " unregister" & vbCrLf & "...or..." & vbCrLf & WScript.ScriptName & _
                " unregister DeviceID" & vbCrLf & vbCrLf & "Available DeviceIDs:" & _
                vbCrLf & vbCrLf

for i = 1 to DevMan.DeviceInfos.Count
    Description = Description & DevMan.deviceInfos(i).DeviceID & " '" & _
                    DevMan.deviceInfos(i).Properties("Name").Value & vbCrLf
next

MsgBox Description
</script>
</job>
```



## Count the Number of Child Items Available for Transfer

The following example shows how to count the number of child items available for transfer on the item returned from ShowSelectItems.


```
Dim dev 'As Device
Dim itms 'As Items
Dim itm 'As Item
Dim i 'As Integer

i = 0
Set dev = CommonDialog1.ShowSelectDevice
Set itms = CommonDialog1.ShowSelectItems(dev, UnspecifiedIntent, _
                                         MaximizeQuality, True)
Set itm = itms(1)

For Each itm In itm.Items
    Dim f
    f = itm.Properties("Item Flags")
    If (f And TransferItemFlag) = TransferItemFlag Then
       i = i + 1
    End If
Next

MsgBox "Selected device has " & i & " child items that can be transferred"
```



## Use a Vector Object

The following example is a contrived sample that shows some of the features of a [**Vector**](-wiaaut-vector.md) object.


```
Dim v 'As Vector

Set v = CreateObject("WIA.Vector")

v.Add 1
v.Add 42
v.Add 3

v.Remove 1
v.Remove 2

MsgBox "v(1) = " & v(1)

v.Clear

v.Add "This"
v.Add "Is"
v.Add "Cool"

v.Remove 1
v.Remove 1

MsgBox "v(1) = " & v(1)
```



 

 




