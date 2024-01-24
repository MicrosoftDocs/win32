---
title: Adding and Modifying the Events
description: Adding and Modifying the Events
ms.assetid: 342b0592-67b7-4c13-bee8-48ac322d3d27
keywords:
- Windows Media Player plug-ins,Echo sample property pages
- plug-ins,Echo sample property pages
- digital signal processing plug-ins,Echo sample property pages
- DSP plug-ins,Echo sample property pages
- Echo DSP plug-in sample,property pages
- Echo DSP plug-in sample,events
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Adding and Modifying the Events

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

You need to supply event handlers for the EN\_CHANGE events that occur when the user changes the text in the property page edit boxes. These event handlers have a simple implementation that merely enables **Apply** in the property page dialog box.

## Modifying the Scale Factor Event Handler

You need to change the name of the existing event handler that the plug-in wizard provided for the scale factor edit box. You should change the name from OnChangeScale to OnChangeDelay in three locations:

1.  In EchoPropPage.h, change the name in the message map macro section. Replace the line that maps the scale factor change event to the OnChangeScale method with the following code:
    ```C++
    COMMAND_HANDLER(IDC_DELAYTIME, EN_CHANGE, OnChangeDelay)
    
    ```

    

2.  In EchoPropPage.h, change the name in the line that prototypes the OnChangeScale function:
    ```C++
    LRESULT (OnChangeDelay)(WORD wNotifyCode, WORD wID, HWND hWndCtl, BOOL& bHandled);
    
    ```

    

3.  In EchoPropPage.cpp, change the name in the function header:
    ```C++
    LRESULT CEchoPropPage::OnChangeDelay(WORD wNotifyCode, WORD wID, HWND hWndCtl, BOOL& bHandled)
    
    ```

    

## Adding the Wet Mix Event Handler

You can easily add the event handler for the EN\_CHANGE event that is attached to the IDC\_WETMIX edit box control. From the dialog resource editor:

1.  Right-click the IDC\_WETMIX edit box and choose **Events**. The New Windows Message and Event Handlers dialog box appears.
2.  In the **Class or object to handle** box, click the name of the edit box resource, IDC\_WETMIX.
3.  In the **New Windows messages/events** box, click EN\_CHANGE to select it.
4.  Click **Add Handler**. The Add Member Function dialog box appears.
5.  In the **Member function name** box, type the name OnChangeWetmix.
6.  Click **OK** to close the Add Member Function dialog box.
7.  Click **OK** to return to the dialog box resource editor.

Visual C++ automatically adds the code for the message map and for the event handler function to EchoPropPage.h. The code it inserts provides a TODO comment where you can add the implementation in the header for the function. This is a slightly different style than the Windows Media Player Plug-in Wizard sample code uses, but is acceptable.

Whether you want to write your implementation in the header file or move it to EchoPropPage.cpp is up to you. In either case, the implementation needs only a single additional line of code to enable **Apply** in the property page dialog. Insert this line of code before the line that returns from the function:


```C++
SetDirty(TRUE);  // Enable Apply.

```



## Related topics

<dl> <dt>

[**Modifying the Echo Sample Property Page**](modifying-the-echo-sample-property-page.md)
</dt> </dl>

 

 




