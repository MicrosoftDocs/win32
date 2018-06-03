---
title: '\_Application Load method'
description: The Load method loads the MMC document from the specified file.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 73be7c9a-080d-49c9-9fe4-932583474ad0
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- Load method MMC
- Load method MMC , Application object
- Application object MMC , Load method
- Load method MMC , _Application interface
- _Application interface MMC , Load method
topic_type:
- apiref
api_name:
- Application.Load
- _Application.Load
api_location:
- Mmc.exe
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# \_Application::Load method

The **Load** method loads the MMC document from the specified file.

## Syntax


```VB
Application.Load( _
  ByVal FileName As String _
)
```



## Parameters

<dl> <dt>

*FileName* 
</dt> <dd>

Name of the file that contains the MMC document.

</dd> </dl>

## Return value

This method does not return a value.

## Examples


```VB
' Load a console file.
objMMC.Load("d:\myapp\console1.msc")
```



## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                        |
| Header<br/>                   | <dl> <dt>MMCObj.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MMCObj.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Mmc.exe</dt> </dl>    |
| CLSID<br/>                    | CLSID\_Application is defined as 49B2791A-B1AE-4C90-9B8E-E860BA07F889<br/>      |
| IID<br/>                      | IID\_\_Application is defined as A3AFB9CC-B653-4741-86AB-F0470EC1384C<br/>      |



 

 





