---
title: Modifying the Echo Dialog Resource
description: Modifying the Echo Dialog Resource
ms.assetid: 2a371004-82a5-42fb-b19c-ea1928a122a1
keywords:
- Windows Media Player plug-ins,Echo sample property pages
- plug-ins,Echo sample property pages
- digital signal processing plug-ins,Echo sample property pages
- DSP plug-ins,Echo sample property pages
- Echo DSP plug-in sample,property pages
- Echo DSP plug-in sample,dialog resource
ms.topic: article
ms.date: 05/31/2018
---

# Modifying the Echo Dialog Resource

You need to change the dialog resource that is the user interface for the property page object. You can first change the existing edit box and label to be useful for the delay time property and then add a second edit box and label for the wet mix property.

To edit the dialog resource in Visual C++:

1.  Click the **ResourceView** tab in the Project Workspace.
2.  Expand the resources tree by opening the top level folder.
3.  Open the **Dialog** folder.
4.  Double-click the dialog resource name, IDD\_ECHOPROPPAGE. The resource editor appears in the right pane.

## Changing the Existing Resources

To change the existing property page resources for the delay time property:

1.  First, change the text in the existing static text control. Right-click the control and then choose **Properties**. In the **Caption** field, type the new caption:
    ```C++
    Delay time (0 to 2000):
    
    ```

    

2.  Close the Text Properties dialog box.
3.  Now, change the name of the edit box control. To do this, right-click the control and then choose **Properties**. In the **ID** field, type a new name for the control:
    ```C++
    IDC_DELAYTIME
    
    ```

    

4.  Close the Edit Properties dialog box.
5.  Save the resource.
6.  Answer **Yes** if prompted to reload the file resource.h.
7.  Click the **FileView** tab in the Project Workspace. Open resource.h
8.  Locate the \#define for the scale factor edit box resource (IDC\_SCALEFACTOR) and delete it. It should have the same id number as IDC\_DELAYTIME.

## Adding the New Resources

To add the new property page resources for the wet mix property:

1.  Click the **ResourceView** tab in the Project Workspace to select it.
2.  Double-click the name of the property page dialog box, IDD\_ECHOPROPPAGE. The resource editor appears in the right pane.
3.  Use the toolbox to add a static text control and an edit box to the property page.
4.  Right-click the static text control and choose **Properties**.
5.  Type a new name for the static text control in the **ID** field:
    ```C++
    IDC_MIXLABEL
    
    ```

    

6.  Type a caption for the label:
    ```C++
    Effect level (%):
    
    ```

    

7.  Close the Text Properties dialog box.
8.  Right-click the edit box and choose **Properties**.
9.  Type a new name for the edit box in the **ID** field:
    ```C++
    IDC_WETMIX
    
    ```

    

10. Close the Edit Properties dialog box.

When you save the project, you may be prompted to reload resource.h. Click **Yes** if this happens. The dialog box resource editor should add the resource names and id numbers to resource.h for the items you added. If for some reason this doesn't happen, you must open resource.h and type new entries for the label and edit box control, and assign each a unique id number.

## Modifying and Adding the String Resources

The plug-in wizard sample code specifies a string resource named IDS\_SCALERANGEERROR that contains a message to display when the user input is out of range. You can modify this resource to suit your needs for the delay time value by following these steps in Visual C++:

1.  Click the **ResourceView** tab.
2.  Open the **String Table** folder.
3.  Double-click the **String Table** icon to open the resource editor.
4.  Double-click the name of the resource you want to edit, in this case, IDS\_SCALERANGEERROR. The String Properties dialog box appears.
5.  Change the name in the **ID** field to IDS\_DELAYRANGEERROR.
6.  Change the text in the **Caption** field:
    ```C++
    You must enter a delay time between 0 and 2000 milliseconds.
    
    ```

    

7.  Close the String Properties dialog box.

Next, add a new string resource for the wet mix property error message.

1.  Double-click the empty line at the bottom of the resource editor.
2.  Change the name in the **ID** field to IDS\_MIXRANGEERROR.
3.  Add the following text to the **Caption** field:
    ```C++
    You must enter an effect level between 0 and 100 percent.
    
    ```

    

4.  Close the String Properties dialog box.

There are two other values you will want to change in the String Table. IDS\_FRIENDLYNAME is the name that appears in the Windows Media Player user interface to identify the plug-in. IDS\_DESCRIPTION lets you tell the user about your plug-in. Both of these strings are passed as parameters to the **IWMPMediaPluginRegistrar::WMPRegisterPlayerPlugin** function, which is called in the DllRegisterServer method in Echodll.cpp.

## Related topics

<dl> <dt>

[**Modifying the Echo Sample Property Page**](modifying-the-echo-sample-property-page.md)
</dt> </dl>

 

 




