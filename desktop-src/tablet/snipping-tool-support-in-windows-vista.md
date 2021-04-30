---
description: This topic describes how your application can specify what URL the Tablet PC Snipping Tool should obtain when capturing your application.
ms.assetid: e31e63e8-8f6b-41f7-8bd6-afc5ca32456b
title: Snipping Tool Support in Windows Vista
ms.topic: article
ms.date: 05/31/2018
---

# Snipping Tool Support in Windows Vista

This topic describes how your application can specify what URL the Tablet PC Snipping Tool should obtain when capturing your application.

## Specifying the URL via Registry Key

Snipping Tool allows users to capture a snip (screen shot) of any object on the screen and then annotate, save, or share the image. When the data is saved in HTML format, or when it is sent to an email client that supports inline HTML, Snipping Tool can add a URL to the snip if the application provides information on how to obtain the URL.

Snipping Tool obtains the URL via accessibility objects. Applications should specify the necessary information under the following registry keys:

HKLM\\Software\\Microsoft\\Windows\\TabletPC\\Snipping Tool\\LinkFingerprints,

And should create a subkey whose name is the same as the window class from which the link should be obtained. The window class name should be the topmost window of the application.

HKLM\\Software\\Microsoft\\Windows\\TabletPC\\Snipping Tool\\LinkFingerprints\\<Window Class Name>

### Window Class Key Details

Under the window class key, the appropriate values should be set in order to indicate Snipping Tool should detect the correct accessibility object.



| VALUE                        | TYPE                  | MASK            | INFORMATION STORED                                          |
|------------------------------|-----------------------|-----------------|-------------------------------------------------------------|
| Mask<br/>              | REG\_DWORD<br/> |                 | Indicates which of the following fields to check<br/> |
| Name<br/>              | REG\_SZ<br/>    | 0x02<br/> | Accessibility name<br/>                               |
| Description<br/>       | REG\_SZ<br/>    | 0x04<br/> | Accessibility description<br/>                        |
| Role<br/>              | REG\_DWORD<br/> | 0x08<br/> | Accessibility role<br/>                               |
| ParentName<br/>        | REG\_SZ<br/>    | 0x10<br/> | Accessibility name of parent<br/>                     |
| ParentValue<br/>       | REG\_SZ<br/>    | 0x20<br/> | Accessibility value of parent<br/>                    |
| ParentRole<br/>        | REG\_DWORD<br/> | 0x40<br/> | Accessibility role of parent<br/>                     |
| ParentDescription<br/> | REG\_SZ<br/>    | 0x80<br/> | Accessibility description of parent<br/>              |



 

Additionally, if the mask bit value 0x1 is set, then the URL should be taken from the accessibility name; otherwise, the URL should be taken from the accessibility value.

If the application uses localized strings for the REG\_SZ values above, the string should be provided as an indirect string by using the following format:

@filename,resource

The string is extracted from the file named, using the resource value as a locator. If the resource value is zero or greater, the number becomes the index of the string in the binary file. If the number is negative, it becomes a resource identifier (ID).

> [!Note]  
> Role constants can be found in oleacc.h in the Windows SDK. The registry values described are specific to Windows Vista.

 

 

 




