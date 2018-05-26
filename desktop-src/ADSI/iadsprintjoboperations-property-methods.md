---
title: IADsPrintJobOperations Property Methods
description: The property methods of the IADsPrintJobOperations interface read and write the properties listed in the following table. For more information about property methods, see Interface Property Methods.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: d1710bd4-e600-4d92-892a-16b4316851d4
ms.prod: windows-server-dev
ms.technology: active-directory-domain-services
ms.tgt_platform: multiple
keywords:
- IADsPrintJobOperations Property Methods ADSI
topic_type:
- apiref
api_name:
- IADsPrintJobOperations Property Methods
- IADsPrintJobOperations.Status
- IADsPrintJobOperations.get_Status
- IADsPrintJobOperations.TimeElapsed
- IADsPrintJobOperations.get_TimeElapsed
- IADsPrintJobOperations.PagesPrinted
- IADsPrintJobOperations.get_PagesPrinted
- IADsPrintJobOperations.Position
- IADsPrintJobOperations.get_Position
- IADsPrintJobOperations.put_Position
api_location:
- Activeds.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# IADsPrintJobOperations Property Methods

The property methods of the [**IADsPrintJobOperations**](/windows/win32/Iads/nn-iads-iadsprintjoboperations?branch=master) interface read and write the properties listed in the following table. For more information about property methods, see [Interface Property Methods](interface-property-methods.md).

## Properties

<dl> <dt>

**PagesPrinted**
</dt> <dd> <dl>

Contains the number of pages printed.

<dt>

Access type: Read-only
</dt> <dt>

Scripting data type: **LONG**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_PagesPrinted(
  [out] LONG* plPagesPrinted
);
```


</dt> </dl> </dd> <dt>

**Position**
</dt> <dd> <dl>

Contains the position of this print job in the print queue.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **LONG**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_Position(
  [out] LONG* plPosition
);
HRESULT put_Position(
  [in] LONG lPosition
);
```


</dt> </dl> </dd> <dt>

**Status**
</dt> <dd> <dl>

Contains the current status of the print job as indicated by one of the [**ADSI Print Job Status Constants**](adsi-print-job-status-constants.md) values.

<dt>

Access type: Read-only
</dt> <dt>

Scripting data type: **LONG**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_Status(
  [out] LONG* plStatus
);
```


</dt> </dl> </dd> <dt>

**TimeElapsed**
</dt> <dd> <dl>

Contains the number of milliseconds elapsed since the print job started.

<dt>

Access type: Read-only
</dt> <dt>

Scripting data type: **LONG**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_TimeElapsed(
  [out] LONG* plTimeElapsed
);
```


</dt> </dl> </dd> </dl>

 

## Examples

The following code example shows how the properties for [**IADsPrintJobOperations**](/windows/win32/Iads/nn-iads-iadsprintjoboperations?branch=master) may be used.


```VB
Dim pqo As IADsPrintQueueOperations
Dim pjo As IADsPrintJobOperations

On Error GoTo Cleanup

Set pqo = GetObject("WinNT://aMachine/aPrinter")
For Each pj In pqo.PrintJobs
    Set pjo = pj
    MsgBox pjo.PagesPrinted & " pages printed for job " & pj.Name
    If (pjo.position > 1) Then
        pjo.Position = pjo.status - 1
    End If
Next

Cleanup:
    If (Err.Number<>0) Then
        MsgBox("An error has occurred. " & Err.Number)
    End If
    Set pqo = Nothing
    Set pjo = Nothing
```



## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                  |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                            |
| Header<br/>                   | <dl> <dt>Iads.h</dt> </dl>         |
| DLL<br/>                      | <dl> <dt>Activeds.dll</dt> </dl>   |
| IID<br/>                      | IID\_IADsPrintJobOperations is defined as 32FB6780-1ED0-11CF-A988-00AA006BC149<br/> |



## See also

<dl> <dt>

[**IADsPrintJob**](/windows/win32/Iads/nn-iads-iadsprintjob?branch=master)
</dt> <dt>

[**IADsPrintJobOperations**](/windows/win32/Iads/nn-iads-iadsprintjoboperations?branch=master)
</dt> <dt>

[**IADsPrintQueue**](/windows/win32/Iads/nn-iads-iadsprintqueue?branch=master)
</dt> <dt>

[**ADSI Print Job Status Constants**](adsi-print-job-status-constants.md)
</dt> </dl>

 

 





