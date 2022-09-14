---
description: Returns the Le field of the application protocol data unit (APDU).
ms.assetid: 249e8105-273b-42f0-9427-9b3cda5bf0a1
title: ISCardCmd::get_LeField method (Scarddat.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ISCardCmd.get_LeField
api_type: 
- COM
api_location: 
- Scardssp.dll
---

# ISCardCmd::get\_LeField method

\[The **get\_LeField** method is available for use in the operating systems specified in the Requirements section. It is not available for use in Windows Server 2003 with Service Pack 1 (SP1) and later, Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The [Smart Card Modules](/previous-versions/windows/desktop/secsmart/smart-card-modules) provide similar functionality.\]

The **get\_LeField** method returns the Le field of the [*application protocol data unit*](../secgloss/a-gly.md) (APDU).

## Syntax


```C++
HRESULT get_LeField(
  [out] LONG *plSize
);
```



## Parameters

<dl> <dt>

*plSize* \[out\]
</dt> <dd>

Pointer to the Le field value on return.

</dd> </dl>

## Return value

The method returns one of the following possible values.



| Return code                                                                                  | Description                                      |
|----------------------------------------------------------------------------------------------|--------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | Operation was completed successfully.<br/> |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | The *plSize* parameter is not valid.<br/>  |



 

## Examples

The following example shows how to retrieve the Le field value from the [*application protocol data unit*](../secgloss/a-gly.md) (APDU). The example assumes that pISCardCmd is a valid pointer to an instance of the [**ISCardCmd**](iscardcmd.md) interface.


```C++
LONG     lLe;
HRESULT  hr;

// Retrieve the Le field value.
hr = pISCardCmd->get_LeField(&lLe);
if (FAILED(hr))
{
    printf("Failed get_LeField\n");
    // Take other error handling action.
}
else
    printf("Le field value returned is %d\n", lLe);
```



## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| End of client support<br/>    | Windows XP<br/>                                                                   |
| End of server support<br/>    | Windows Server 2003<br/>                                                          |
| Header<br/>                   | <dl> <dt>Scarddat.h</dt> </dl>   |
| Type library<br/>             | <dl> <dt>Scarddat.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Scardssp.dll</dt> </dl> |
| IID<br/>                      | IID\_ISCardCmd is defined as D5778AE3-43DE-11D0-9171-00AA00C18068<br/>            |



## See also

<dl> <dt>

[**ISCardCmd**](iscardcmd.md)
</dt> </dl>

 

 
