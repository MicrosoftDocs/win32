---
Description: This sample shows how to use Ink Analysis to create a form-filling application, where the form is based on a scanned paper form.
ms.assetid: 1eae5962-b4e0-4947-a6d2-63713a68198c
title: Ink Analysis Scanned Paper Form
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Ink Analysis Scanned Paper Form

This sample shows how to use Ink Analysis to create a form-filling application, where the form is based on a scanned paper form.

## Features Demonstrated

This sample application demonstrates the following features of the Ink Analysis API and the Windows Forms Ink Controls:

-   Loading a scanned paper form. The sample imports the form from an image in .png format.
-   Collecting and rendering ink on top of the scanned form.
-   Using an [InkAnalyzer](https://msdn.microsoft.com/library/ms583671(v=VS.90).aspx) object to parse handwriting.
-   Generating [AnalysisHintNode](https://msdn.microsoft.com/library/ms573018(v=VS.90).aspx) objects to improve handwriting results.
-   Populating text boxes from analysis hints.
-   Creating a basic text correction experience.

## Project References

The sample is available as a Windows Forms or Windows Presentation Foundation application. The Windows Forms version references:

-   Microsoft.Ink.dll
-   Microsoft.Ink.Analysis.dll

The Windows Presentation Foundation version references IAWinFX.dll in addition to the core Windows Presentation Foundation dlls.

> [!Note]  
> The Windows Presentation Foundation version of this sample (found in the XAML directory) requires that the Windows Presentation Foundation extensions for Microsoft Visual Studio 2005 is installed on the system.

 

## User Interface

The UI for this application consists of a [TabControl](https://msdn.microsoft.com/library/8fb09fh2(v=VS.90).aspx) with two [TabPage](https://msdn.microsoft.com/library/s78d0xf0(v=VS.90).aspx) objects associated with it: Ink Form and Converted Text Form. The Ink Form tab contains

-   A panel that contains an image of a scanned paper form used for taking telephone messages.
-   A check box that has the application show the analysis hint bounds when selected.
-   A pair of buttons, Clear and Analyze, that clear the ink from the form and initialize ink analysis.

The Converted Text Form contains the same image and is the page on which the application displays the recognized text. When you click Analyze, the application performs ink analysis synchronously, and the recognition results appear on the Converted Text Form tab.

## Functionality

This application uses an [InkOverlay](https://msdn.microsoft.com/library/ms552322(v=VS.90).aspx) to enable writing. The InkOverlay object is well suited for note taking and basic scribbling. The primary intended use of this object is to display ink as ink. The main class for ink analysis is the [InkAnalyzer](https://msdn.microsoft.com/library/ms583671(v=VS.90).aspx) class. When you call the InkAnalyzer object's [Analyze](https://msdn.microsoft.com/library/ms568971(v=VS.90).aspx) method, the ink analysis occurs synchronously.

The application initializes two arrays, one of strings and one of rectangles. The string array, `factoidStrings`, is made of [Factoid](https://msdn.microsoft.com/library/ms583657(v=VS.90).aspx) objects that are passed into the [InkAnalyzer](https://msdn.microsoft.com/library/ms583671(v=VS.90).aspx) as [AnalysisHintNode](https://msdn.microsoft.com/library/ms573018(v=VS.90).aspx) objects. The AnalysisHintNode objects bias the InkAnalyzer toward particular input. This sample uses the date, time, and telephone hints, as well as some others.

Each [AnalysisHintNode](https://msdn.microsoft.com/library/ms573018(v=VS.90).aspx) is associated with a specific area of the form. The areas are represented by the array of rectangles, `rects`. By creating a [TextBox](https://msdn.microsoft.com/library/48deaakc(v=VS.90).aspx) for each rectangle, the sample outputs the recognized text in the correct location.


```C++
        private void InitHints()
        {
            // Instantiate the collection of TextBoxes.
            this.textBoxes = new ArrayList();

            // For each Rectangle in Rectangles
            for (int i = 0; i < rects.Length; i++)
            {

                Rectangle rectangle = rects[i];

                // Create an AnalysisHintNode with the bounds of the Rectangle.  The bounds
                // of an AnalysisHintNode gives clues to the handwriting recognizer about
                // the way Strokes are grouped together.
                AnalysisHintNode hint = this.analyzer.CreateAnalysisHint(rectangle);

                // Set the corresponding Factoid on the AnalysisHintNode.  This gives the 
                // recognizer clues about the meaning of the strokes within the 
                // AnalysisHintNode's region.
                hint.Factoid = factoidStrings[i];

                // Create a corresponding TextBox where the results of the analysis
                // associated with this AnalysisHintNode will be displayed.  Store the reference
                // to the TextBox in the textBoxes Collection.
                this.textBoxes.Add(InitTextBox(hint));
            }
        }
```



After that, it is merely a matter of creating an event handler that triggers the ink analysis when the user clicks Analyze.


```C++
        private void UpdateTextBoxes()
        {
            // Get the AnalysisHintNodes that we previously added to the InkAnalyzer.
            ContextNodeCollection hints = this.analyzer.GetAnalysisHints();

            for (int i = 0; i < hints.Count; i++)
            {
                // Get the recognized string from the AnalysisHintNode
                string analyzedString = ((AnalysisHintNode)hints[i]).GetRecognizedString();

                // If we found a string, set the contents of the TextBox
                // to that string.
                if (analyzedString != null)
                {
                    ((TextBox)this.textBoxes[i]).Text = analyzedString;
                }
            }
        }
```



 

 



