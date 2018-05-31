---
error-parsing-yaml: 
---

# IVMHostInfo::IsHostDriveMounted method

The **IsHostDriveMounted** method indicates whether the specified host drive is mounted.

## Syntax


```C++
HRESULT IsHostDriveMounted(
  [in]  BSTR         hostDriveIdentifier,
  [out] VARIANT_BOOL *hostDriveMounted
);
```



## Parameters

<dl> <dt>

*hostDriveIdentifier* \[in\]
</dt> <dd>

The desired host drive to check. The [**HostDrives**](ivmhostinfo-hostdrives.md) property is used to retrieve a list of valid drive identifier strings.

</dd> <dt>

*hostDriveMounted* \[out\]
</dt> <dd>

**VARIANT\_TRUE** if the host drive specified by *hostDriveIdentifier* is mounted, **VARIANT\_FALSE** if otherwise.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code                                                                                       | Description                                                                                   |
|---------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>              | The operation was successful.<br/>                                                      |
| <dl> <dt>**E\_POINTER**</dt> </dl>         | The *hostDriveIdentifier* or *hostDriveMounted* parameter is **NULL**.<br/>             |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>      | The *hostDriveIdentifier* parameter is empty or does not reference a usable drive.<br/> |
| <dl> <dt>**DISP\_E\_EXCEPTION**</dt> </dl> | An unexpected error has occurred.<br/>                                                  |



 

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMHostInfo**](ivmhostinfo.md)
</dt> </dl>

 

 





