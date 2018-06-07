---
Description: This application demonstrates how you can build a handwriting recognition application.The Windows Vista SDK provides versions of this sample in C\# and Visual Basic .NET, as well.
ms.assetid: 4b3fc078-731e-4263-8e95-2c273d69a457
title: Ink Recognition Sample
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Ink Recognition Sample

This application demonstrates how you can build a handwriting recognition application.The Windows Vista SDK provides versions of this sample in C\# and Visual Basic .NET, as well. This topic refers to the Visual Basic .NET sample, but the concepts are the same between versions.

## Access the Tablet PC Interfaces

First, reference the Tablet PC API, which are installed with the SDK.


```VB
' The Ink namespace, which contains the Tablet PC Platform API
Imports Microsoft.Ink
```



## Initialize the InkCollector

The sample adds code to the form's [Load](https://www.bing.com/search?q=Load) event handler that serves to associate the [InkCollector](https://www.bing.com/search?q=InkCollector), myInkCollector, with the group box window and enable the InkCollector.


```VB
Private Sub InkRecognition_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load

   ' Create the recognizers collection
    myRecognizers = New Recognizers()

    ' Create an ink collector that uses the group box handle
    myInkCollector = New InkCollector(gbInkArea.Handle)

    ' Turn the ink collector on
    myInkCollector.Enabled = True

End Sub
```



## Recognize the Strokes

The [Button](https://www.bing.com/search?q=Button) object's [Click](https://www.bing.com/search?q=Click) event handler checks to ensure that the user has at least one recognizer installed by examining the [Count](https://www.bing.com/search?q=Count) property of the [Recognizers](https://www.bing.com/search?q=Recognizers) collection.

The [SelectedText](https://www.bing.com/search?q=SelectedText) property of the text box is set to the best match for the strokes using the [ToString](https://www.bing.com/search?q=ToString) method on the [Strokes](https://www.bing.com/search?q=Strokes) collection. After the strokes have been recognized, they are deleted. Finally, the code forces drawing area repaint, clearing it for further ink use.


```VB
Private Sub btnRecognize_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles btnRecognize.Click

    ' Check to ensure that the user has at least one recognizer installed
    ' Note that this is a preventive check - otherwise, an exception 
    ' occurs during recognition
    If 0 = myRecognizers.Count Then
        MessageBox.Show("There are no handwriting recognizers installed.  You need to have at least one in order to run this sample.")
    Else
        ' ...
        txtResults.SelectedText = myInkCollector.Ink.Strokes.ToString

        ' If the mouse is pressed, do not perform the recognition -
        ' this prevents deleting a stroke that is still being drawn
        If Not myInkCollector.CollectingInk Then

            ' Delete the ink from the ink collector
            myInkCollector.Ink.DeleteStrokes(myInkCollector.Ink.Strokes)

            ' Force the Frame to redraw (so the deleted ink goes away)
            gbInkArea.Refresh()

        End If
    End If
End Sub
```



## Closing the Form

The form's [Dispose](https://www.bing.com/search?q=Dispose) method disposes the [InkCollector](https://www.bing.com/search?q=InkCollector) object.

 

 



