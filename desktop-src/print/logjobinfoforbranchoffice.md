---
Description: 'Allows Branch Office clients to send job events to the host print server.'
ms.assetid: '6D1AB299-2E26-42AF-9613-CA321173080D'
title: LogJobInfoForBranchOffice function
---

# LogJobInfoForBranchOffice function

Allows Branch Office clients to send job events to the host print server.

## Syntax


```C++
HRESULT WINAPI LogJobInfoForBranchOffice(
  _In_ HANDLE                        hPrinter,
  _In_ PBranchOfficeJobDataContainer pJobDataContainer
);
```



## Parameters

<dl> <dt>

*hPrinter* \[in\]
</dt> <dd>

Specifies a handle to the CSR printer.

</dd> <dt>

*pJobDataContainer* \[in\]
</dt> <dd>

Specifies a pointer to an array of [**BranchOfficeJobData**](RID) structures, containing the events to be logged.

</dd> </dl>

## Return value

Indicates success or failure.

## Requirements



|                   |                                                                                      |
|-------------------|--------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Winsplp.h</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20LogJobInfoForBranchOffice%20function%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




