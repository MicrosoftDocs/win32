---
Description: Sets the first parameter (P1) byte of the application protocol data unit (APDU).
ms.assetid: 359df5cc-10a7-4093-9a77-f3eb0b98545a
title: ISCardCmd::put\_P1 method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ISCardCmd::put\_P1 method

\[The **put\_P1** method is available for use in the operating systems specified in the Requirements section. It is not available for use in Windows Server 2003 with Service Pack 1 (SP1) and later, Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The [Smart Card Modules](https://msdn.microsoft.com/a33e4e23-5f0d-4d03-ae3b-8727cdf57ab7) provide similar functionality.\]

The **put\_P1** method sets the first parameter (P1) byte of the [*application protocol data unit*](https://msdn.microsoft.com/0baaa937-f635-4500-8dcd-9dbbd6f4cd02) (APDU).

## Syntax


```C++
HRESULT put_P1(
  [in] BYTE byP1
);
```



## Parameters

<dl> <dt>

*byP1* \[in\]
</dt> <dd>

The byte that is the P1 field.

</dd> </dl>

## Return value

The method returns one of the following possible values.



| Return code                                                                                   | Description                                   |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Operation completed successfully.<br/>  |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | The *byP1* parameter is not valid.<br/> |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Out of memory.<br/>                     |



 

## Remarks

To set the P2 value of the APDU, call [**get\_P2**](iscardcmd-get-p2.md).

To retrieve the existing P1, P2, and P3 values, call [**get\_P1**](iscardcmd-get-p1.md), [**get\_P2**](iscardcmd-get-p2.md) or [**get\_P3**](iscardcmd-get-p3.md) respectively.

For a list of all the methods provided by this interface, see [**ISCardCmd**](iscardcmd.md).

In addition to the COM error codes listed above, this interface may return a [*smart card*](https://msdn.microsoft.com/3e9d7672-2314-45c8-8178-5a0afcfd0c50) error code if a smart card function was called to complete the request. For more information, see [Smart Card Return Values](authentication-return-values.md).

## Examples

The following example shows how to set the first parameter (P1) byte of the [*application protocol data unit*](https://msdn.microsoft.com/0baaa937-f635-4500-8dcd-9dbbd6f4cd02) (APDU). The example assumes that pISCardCmd is a valid pointer to an instance of the [**ISCardCmd**](iscardcmd.md) interface.


```C++
HRESULT  hr;

// Set the P1 byte.
hr = pISCardCmd->put_P1(0x06);
if (FAILED(hr))
{
  printf("Failed put_P1\n");
  // Take other error handling action as needed.
}
```



## Requirements



|                                     |                                                                                         |
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

[**get\_P1**](iscardcmd-get-p1.md)
</dt> <dt>

[**get\_P2**](iscardcmd-get-p2.md)
</dt> <dt>

[**get\_P3**](iscardcmd-get-p3.md)
</dt> <dt>

[**ISCardCmd**](iscardcmd.md)
</dt> <dt>

[**put\_P2**](iscardcmd-put-p2.md)
</dt> </dl>

 

 




