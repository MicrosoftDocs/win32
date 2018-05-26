---
title: Creating the MSVidWebDVD Object
description: Creating the MSVidWebDVD Object
ms.assetid: 3ea19c61-c4f0-4f41-9089-db1c8cb22579
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Creating the MSVidWebDVD Object

This topic applies to Windows XP Service Pack 1 or later.

This article describes how to instantiate the **MSVidWebDVD** object and associated objects for DVD playback.

> [!Note]  
> Neither Windows XP nor the DirectX SDK offers an MPEG-2 decoder for writing DVD applications. Many DVD hardware providers offer hardware or software decoding options, and many DVDs come packaged with a DVD decoder.

 

The Video Control's DVD helper object is **MSVidWebDVD**. The **MSVidWebDVD** object is used only as a DVD controller—it is not represented on the screen—and it is instantiated programmatically. One other object, **MSVidWebDVDAdm**, is also used for some DVD tasks and is also instantiated in code.

The following list summarizes the steps necessary to create the objects for viewing DVD content in a Windows form or HTML page. Details follow the list.

1.  Add the **MSVidCtl** object to your form.
2.  Add features, such as closed captions, to **MSVidCtl**.
3.  Build the filter graph.
4.  Instantiate the **MSVidWebDVD** and **MSVidWebDVDAdm** objects.
5.  Run the graph.

First, create a Visual Basic project and add the MS Video Control 1.0 Type Library to your project as a reference and a component. See [DVD Applications in Visual Basic (Video Control)](dvd-applications-in-visual-basic--video-control.md) for system requirements. Draw the **MSVidCtl** object, also called the Video Control, onto your form and give it a name, for example "oVideoControl".

If you wish to support closed captions, you can programmatically add the closed captioning feature to **MSVidCtl**. The following code shows a subroutine to add closed captioning:


```C++
Private g_msCC as MSVidClosedCaptioning
Sub AddCC()
   Dim oFeature As IMSVidFeature
   Dim oFeatureColl As New MSVidFeatures
   'Closed captioning GUID
   Const CLSID_CC = "{7F9CB14D-48E4-43B6-9346-1AEBC39C64D3}"

   For Each oFeature In oVideoControl.FeaturesAvailable
       If oFeature.ClassID = CLSID_CC Then
           oVideoControl.FeaturesActive.Add oFeature
           oFeatureColl.Add oFeature
           Set g_msCC = oFeature
       End If
   Next oFeature
End Sub
' Enable or disable closed captioning by setting 
' g_msCC.Enable = True or False. May be done during playback.
```



Finally, build the filter graph and create the **MSVidWebDVD** and **MSVidWebAdm** objects. These objects are used to control most DVD functions. The **MSVidWebDVD** object can be created either by iterating through the **MSVidCtl** object's input types and searching for the DVD player, or by directly calling the **View** command on the **MSVidCtl** object, specifying the DVD player as the input device. This second, shorter method automates the iteration and makes accessing the DVD player quite simple.

The following code illustrates the short way to create the **MSVidWebDVD** object and the **MSVidWebAdm** object. The **View**, **Build**, and **Run** commands automate graph creation. The **AddCC** subroutine called is the one shown in the previous example.


```C++
Option Explicit
' Create the DVD and Adm objects. Be sure to create the DVD using
' WithEvents to access object-specific events.
Dim WithEvents oVidWebDVD As MSVidWebDVD
Dim oVidWebAdm As MSVidWebDVDAdm

' Build the graph to prepare for playback. Does not start playback.
Sub BuildGraph()
   ' First insert the DVD Navigator filter.
   oVideoControl.View ("DVD:")

   ' Then enable closed-captioning feature. 
   ' All features must be added before Build or Run methods.
   Call AddCC

   ' Next build the graph.
   oVideoControl.Build

   ' Finally, instantiate the control objects.
   Set oVidWebDVD = oVideoControl.InputActive
   Set oVidWebAdm = oVidWebDVD.DVDAdm
 End Sub

' Start playback from Play button.
Sub cmdRun_Click()
   oVideoControl.Run
End Sub
```



## Related topics

<dl> <dt>

[DVD Applications in Visual Basic (Video Control)](dvd-applications-in-visual-basic--video-control.md)
</dt> </dl>

 

 




