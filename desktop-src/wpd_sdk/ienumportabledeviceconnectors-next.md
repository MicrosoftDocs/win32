---
description: Retrieves the next one or more IPortableDeviceConnector objects in the enumeration sequence.
ms.assetid: 5aed563a-5ecc-49c0-8a0c-622405453896
title: IEnumPortableDeviceConnectors::Next method (Devpkey.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IEnumPortableDeviceConnectors.Next
api_type: 
- COM
api_location: 
- PortableDeviceGuids.lib
- PortableDeviceGuids.dll
---

# IEnumPortableDeviceConnectors::Next method

The **Next** method retrieves the next one or more [**IPortableDeviceConnector**](/windows/desktop/api/portabledeviceconnectapi/nn-portabledeviceconnectapi-iportabledeviceconnector) objects in the enumeration sequence.

## Syntax


```C++
HRESULT Next(
  [in]      UINT32                   cRequested,
  [out]     IPortableDeviceConnector **pConnectors,
  [in, out] UINT32                   *pcFetched
);
```



## Parameters

<dl> <dt>

*cRequested* \[in\]
</dt> <dd>

The number of requested devices. This value also indicates the number of elements in the caller-allocated array specified by the *pConnectors* parameter.

</dd> <dt>

*pConnectors* \[out\]
</dt> <dd>

An array of [**IPortableDeviceConnector**](/windows/desktop/api/portabledeviceconnectapi/nn-portabledeviceconnectapi-iportabledeviceconnector) pointers, each specifying a paired MTP Bluetooth device. The caller must allocate an array of **IPortableDeviceConnector** pointers, with the array length specified by the *cRequested* parameter. On successful return, the caller must free both the array and the returned pointers. The **IPortableDeviceConnector** interfaces are freed by calling the **IUnknown::Release** method.

</dd> <dt>

*pcFetched* \[in, out\]
</dt> <dd>

The number of [**IPortableDeviceConnector**](/windows/desktop/api/portabledeviceconnectapi/nn-portabledeviceconnectapi-iportabledeviceconnector) interfaces that are actually retrieved. If no **IPortableDeviceConnector** interfaces are retrieved and the return value is **S\_FALSE**, there are no more **IPortableDeviceConnector** interfaces to enumerate.

</dd> </dl>

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                             | Description                                                      |
|-----------------------------------------------------------------------------------------|------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>    | The method succeeded.<br/>                                 |
| <dl> <dt>**S\_FALSE**</dt> </dl> | There are no more MTP Bluetooth devices to enumerate.<br/> |



 

## Examples

The following example demonstrates the use of this method to enumerate paired MTP/Bluetooth devices, and to send an asynchronous connection request to each.


```C++
IEnumPortableDeviceConnectors* pEnum = NULL;
    HRESULT hrEnum = S_OK;
 HRESULT hr = CoCreateInstance(CLSID_EnumBthMtpConnectors, NULL, CLSCTX_INPROC_SERVER, IID_PPV_ARGS(&pEnum));
    if (SUCCEEDED(hr))
{
  while (S_OK == hrEnum)
    {
       UINT32  uFetched        = 0;
       LPWSTR  wszDevicePnPID  = NULL;
       IPortableDeviceConnector* pDevice = NULL;
       hrEnum = pEnum->Next(1, &spDevice, &uFetched);
       if (hrEnum == S_OK && uFetched == 1)
        {
          // Send an asynchronous connect request.  
          hr = pDevice ->Connect(NULL);
          // Release the device when done
          pDevice->Release();
          pDevice = NULL;
        }
     }  // while S_OK == hrEnum
  // Release the enumerator when done
    if (pEnum)
    {
     pEnum->Release();
     pEnum = NULL;
   }
    }
       
```



## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                                                                                             |
| Minimum supported server<br/> | None supported<br/>                                                                                                                                              |
| Header<br/>                   | <dl> <dt>Devpkey.h; </dt> <dt>Portabledeviceconnectapi.h</dt> </dl> |
| IDL<br/>                      | <dl> <dt>Portabledeviceconnectapi.idl</dt> </dl>                                                                |
| Library<br/>                  | <dl> <dt>PortableDeviceGuids.lib</dt> </dl>                                                                     |



## See also

<dl> <dt>

[**IEnumPortableDeviceConnectors**](ienumportabledeviceconnectors.md)
</dt> </dl>

 

 




