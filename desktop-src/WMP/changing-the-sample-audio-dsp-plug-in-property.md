---
title: Changing the Sample Audio DSP Plug-in Property
description: Changing the Sample Audio DSP Plug-in Property
ms.assetid: 9e742bcd-cff8-422f-ad91-d8d46f15bdc4
keywords:
- Windows Media Player plug-ins,audio DSP
- plug-ins,audio DSP
- digital signal processing plug-ins,audio properties
- DSP plug-ins,audio properties
- audio DSP plug-ins,properties
ms.topic: article
ms.date: 05/31/2018
---

# Changing the Sample Audio DSP Plug-in Property

You will probably want to change the property that the Windows Media Player Plug-in Wizard creates by default. The following list details the items that might require changing:

-   **The dialog resource.** Click the **ResourceView** tab in the Project Workspace window. Expand the folder list to open the Dialog folder. Double-click the dialog resource to open the resource editor. You can make changes to the property page dialog to fulfill your needs. For instance, you could change the text in the label or replace the edit control with a checkbox.
-   **The property page object code.** The default implementation uses a variable of type double to store the scale factor. You might require a different type of data. This would also require you to change the code that persists the data to the registry and reads the data from the registry (including the code that reads from the registry in *CProjectName*::**FinalConstruct**).
-   **The member variable that stores the property value.** This variable is named "m\_fScaleFactor" and is declared as type double. You may want to change the name and type of this variable throughout the project.
-   **The property get and property put methods.** You might want to change the names, parameters, and implementations of these methods. Don't forget to also reflect those changes elsewhere in the project. For instance, the property page **Apply** method calls *CProjectName*::**put\_scale**.

## Related topics

<dl> <dt>

[**Implementing an Audio DSP Plug-in**](implementing-an-audio-dsp-plug-in.md)
</dt> </dl>

 

 




