---
title: ICatalog OpenMshx method
description: method OpenMshx - opens an MSHX catalog given a valid path to the MSHX file
ms.assetid: 13ff1831-8f20-47be-af2d-7b689c5b597f
keywords:
- OpenMshx method HelpAPI
- OpenMshx method HelpAPI , ICatalog interface
- ICatalog interface HelpAPI , OpenMshx method
topic_type:
- apiref
api_name:
- ICatalog.OpenMshx
api_location:
- Windows.Help.Runtime.idl
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ICatalog::OpenMshx method

method OpenMshx - opens an MSHX catalog given a valid path to the MSHX file

## Syntax


```C++
HRESULT OpenMshx(
  [in] BSTR path
);
```



## Parameters

<dl> <dt>

*path* \[in\]
</dt> <dd></dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                          |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                |
| IDL<br/>                      | <dl> <dt>Windows.Help.Runtime.idl</dt> </dl> |



## See also

<dl> <dt>

[**ICatalog**](icatalog.md)
</dt> </dl>

 

 





