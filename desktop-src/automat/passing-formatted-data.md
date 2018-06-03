---
title: Passing Formatted Data
description: When handling formatted data, the application should pass an object that implements the OLE IDataObject interface.
ms.assetid: 2226d0b5-2860-49be-896a-f26038947660
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Passing Formatted Data

Often, an application needs to accept formatted data as an argument to a method or property. Examples include a bitmap, formatted text, or a spreadsheet range. When handling formatted data, the application should pass an object that implements the OLE **IDataObject** interface. For detailed information about the interface, see the *COM Programmer's Reference*.

By using this interface, applications can retrieve the data of any Clipboard format. Because an **IDataObject** instance can provide data of more than one format, a caller can provide data in several formats, and let the called object choose which format is most appropriate.

If the data object implements [**IDispatch**](/previous-versions/windows/desktop/api/oaidl/nn-oaidl-idispatch), it should be passed using the VT\_DISPATCH flag. If the data object does not support **IDispatch**, it should be passed with the VT\_UNKNOWN flag.

 

 




