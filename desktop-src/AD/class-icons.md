---
title: Class Icons
description: The icon used to represent a class object can be specified in the iconPath attribute in the DisplaySpecifiers container.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 0ff8da8a-d3d3-4a15-8103-4fe6ec307427
ms.tgt_platform: multiple
keywords:
- class display names AD ,icons
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Class Icons

The icon used to represent a class object can be specified in the **iconPath** attribute in the DisplaySpecifiers container. Moreover, each class can store multiple icon states. For example, a folder class can have icons for the open, closed, and disabled states. The current implementation accepts a maximum of sixteen different icon states per class.

The **iconPath** attribute can be specified in one of two ways.


```C++
<state>,<icon file name>
```



or


```C++
<state>,<module file name>,<resource ID>
```



In these examples, the "<state>" is an integer with a value between 0 and 15. The value 0 is defined to be the default or closed state of the icon. The value 1 is defined to be the open state of the icon. The value 2 is the disabled state. All other values are application-defined.

The "<icon file name>" is the path and file name of an icon file that contains the icon image.

The "<module file name>" is the path and file name of a module, such as an EXE or DLL, that contains the icon image in a resource. The "<resource ID>" is an integer that specifies the resource identifier of the icon resource within the module.

## Adding a Value to the **iconPath** Attribute

To add a value to the **iconPath** attribute, perform the following steps.

1.  Determine if the value for the attribute exists. If a value is to be replaced, first, delete the existing value using the [**IADs::PutEx**](https://msdn.microsoft.com/library/aa746353) method with the *lnControlCode* parameter set to **ADS\_PROPERTY\_DELETE** and the *vProp* parameter set to the value to be removed. Do not use **ADS\_PROPERTY\_CLEAR** or **ADS\_PROPERTY\_UPDATE** for *lnControlCode*.
2.  Create the string that represents the attribute icon data. For an example, see the format above.
3.  To add the new value, use the [**IADs::PutEx**](https://msdn.microsoft.com/library/aa746353) method with the *lnControlCode* parameter set to **ADS\_PROPERTY\_APPEND**.
4.  To commit changes to the directory, call [**IADs::SetInfo**](https://msdn.microsoft.com/library/aa746354).

 

 




