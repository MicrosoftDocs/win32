---
Description: Initializes or reinitializes the system image list.
ms.assetid: 4e661326-157e-4c75-86df-cd213e01c3e5
title: FileIconInit function
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- FileIconInit
api_type: 
- DllExport
api_location: 
- Shell32.dll
---

# FileIconInit function

Initializes or reinitializes the system image list.

## Syntax


```C++
BOOL FileIconInit(
  _In_ BOOL fRestoreCache
);
```



## Parameters

<dl> <dt>

*fRestoreCache* \[in\]
</dt> <dd>

Type: **BOOL**

**TRUE** to restore the system image cache from disk; **FALSE** otherwise.

</dd> </dl>

## Return value

Type: **BOOL**

**TRUE** if the cache was successfully refreshed, **FALSE** if the initialization failed.

## Remarks

If you are using system image lists in your own process, you must call **FileIconInit** at the following times:

-   On launch.
-   In response to a [**WM\_SETTINGCHANGE**](https://msdn.microsoft.com/en-us/library/ms725497(v=VS.85).aspx) message when the [**SPI\_SETNONCLIENTMETRICS**](https://msdn.microsoft.com/library/ms724947(v=VS.85).aspx) flag is set.

**FileIconInit** is not included in a header file. You must call it directly from Shell32.dll, using ordinal 660.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                   |
| DLL<br/>                      | <dl> <dt>Shell32.dll</dt> </dl> |



 

 




