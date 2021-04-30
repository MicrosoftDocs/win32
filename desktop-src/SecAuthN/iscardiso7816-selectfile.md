---
description: The SelectFile method constructs an application protocol data unit (APDU) command that sets a current elementary file within a logical channel. Subsequent commands may implicitly refer to the current file through the logical channel.
ms.assetid: cb6231b3-fb1c-4350-8797-9efaa663c21b
title: ISCardISO7816::SelectFile method (Scardssp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ISCardISO7816.SelectFile
api_type: 
- COM
api_location: 
- Scardssp.dll
---

# ISCardISO7816::SelectFile method

\[The **SelectFile** method is available for use in the operating systems specified in the Requirements section. It is not available for use in Windows Server 2003 with Service Pack 1 (SP1) and later, Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The [Smart Card Modules](/previous-versions/windows/desktop/secsmart/smart-card-modules) provide similar functionality.\]

The **SelectFile** method constructs an [*application protocol data unit*](../secgloss/a-gly.md) (APDU) command that sets a current elementary file within a logical channel. Subsequent commands may implicitly refer to the current file through the logical channel.

Selecting a directory (DF) within the card filestore — which may be the root (MF) of the filestore — makes it the current DF. After such a selection, an implicit current elementary file may be referred to through that logical channel.

Selecting an elementary file sets the selected file and its parent as current files.

After the answer to reset, the MF is implicitly selected through the basic logical channel, unless specified differently in the historical bytes or in the initial data string.

## Syntax


```C++
HRESULT SelectFile(
  [in]      BYTE         byP1,
  [in]      BYTE         byP2,
  [in]      LPBYTEBUFFER pData,
  [in]      LONG         lBytesToRead,
  [in, out] LPSCARDCMD   *ppCmd
);
```



## Parameters

<dl> <dt>

*byP1* \[in\]
</dt> <dd>

Selection control.



| P1 (upper byte in word): 8 7 6 5 4 3 2 1                                                                                                                                                            | Meaning                            |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------|
| <span id="000000xx"></span><span id="000000XX"></span><dl> <dt>**000000xx**</dt> <dt></dt> </dl> | Select File ID<br/>          |
| <span id="00000000"></span><dl> <dt>**00000000**</dt> <dt></dt> </dl>                            | EF, DF, or MF<br/>           |
| <span id="00000001"></span><dl> <dt>**00000001**</dt> <dt></dt> </dl>                            | Child DF<br/>                |
| <span id="00000010"></span><dl> <dt>**00000010**</dt> <dt></dt> </dl>                            | EF under DF<br/>             |
| <span id="00000011"></span><dl> <dt>**00000011**</dt> <dt></dt> </dl>                            | Parent DF of current DF<br/> |



 

When P1=00, the card knows either because of a specific coding of the file ID or because of the context of execution of the command if the file to select is the MF, a DF, or an EF.

When P1-P2=0000, if a file ID is provided, then it shall be unique in the following environments:

-   Immediate children of the current DF
-   Parent DF
-   Immediate children of the parent DF

If P1-P2=0000 and if the data field is empty or equal to 3F00, then select the MF.

When P1=04, the data field is a DF name, possibly right truncated.

When supported, successive such commands with the same data field shall select DFs whose names match with the data field (that is, start with the command data field). If the card accepts the command with an empty data field, then all or a subset of the DFs can be successively selected.

</dd> <dt>

*byP2* \[in\]
</dt> <dd>

Selection control.

</dd> <dt>

*pData* \[in\]
</dt> <dd>

Data for operation if needed; else, **NULL**. Types of data that are passed in this parameter include:

-   file ID
-   path from the MF
-   path from the current DF
-   DF name

</dd> <dt>

*lBytesToRead* \[in\]
</dt> <dd>

Empty (that is, 0) or maximum length of data expected in response.

</dd> <dt>

*ppCmd* \[in, out\]
</dt> <dd>

On input, a pointer to an [**ISCardCmd**](iscardcmd.md) interface object or **NULL**.

On return, it is filled with the APDU command constructed by this operation. If *ppCmd* was set to **NULL**, a [*smart card*](../secgloss/s-gly.md) [**ISCardCmd**](iscardcmd.md) object is internally created and returned via the *ppCmd* pointer.

</dd> </dl>

## Return value

The method returns one of the following possible values.



| Return code                                                                                   | Description                                  |
|-----------------------------------------------------------------------------------------------|----------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Operation completed successfully.<br/> |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | Invalid parameter.<br/>                |
| <dl> <dt>**E\_POINTER**</dt> </dl>     | A bad pointer was passed in.<br/>      |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Out of memory.<br/>                    |



 

## Remarks

Unless otherwise specified, the correct execution of the encapsulated command modifies the security status according to the following rules:

-   When the current elementary file is changed, or when there is no current elementary file, the security status specific to a former current elementary file is lost.
-   When the current filestore directory (DF) is descendant of, or identical to the former current DF, the security status specific to the former current DF is lost. The security status common to all common ancestors of the previous and new current DF is maintained.

For a list of all the methods provided by this interface, see [**ISCardISO7816**](iscardiso7816.md).

In addition to the COM error codes listed above, this interface may return a smart card error code if a smart card function was called to complete the request. For more information, see [Smart Card Return Values](authentication-return-values.md).

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| End of client support<br/>    | Windows XP<br/>                                                                   |
| End of server support<br/>    | Windows Server 2003<br/>                                                          |
| Header<br/>                   | <dl> <dt>Scardssp.h</dt> </dl>   |
| Type library<br/>             | <dl> <dt>Scardsrv.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Scardssp.dll</dt> </dl> |
| IID<br/>                      | IID\_ISCardISO7816 is defined as 53B6AA68-3F56-11D0-916B-00AA00C18068<br/>        |



## See also

<dl> <dt>

[**ISCardISO7816**](iscardiso7816.md)
</dt> </dl>

 

 
