---
description: Issuing the GetNumObjects Command
ms.assetid: d06690e4-f592-4b17-a5f1-baec2accc8dd
title: Issuing the GetNumObjects Command
ms.topic: article
ms.date: 05/31/2018
---

# Issuing the GetNumObjects Command

The example in this section invokes the **GetNumObjects** MTP command. (For a complete description of this command and its parameters, see the [MTP specification](https://www.usb.org/sites/default/files/MTPv1_1.zip).)

Before you invoke this command, you must first set up the command parameters.


```
#include <portabledevice.h>
#include <portabledeviceapi.h>
#include <wpdmtpextensions.h>

HRESULT SendGetNumObjects(IPortableDevice* pDevice)
{
    HRESULT hr = S_OK;
    const WORD PTP_OPCODE_GETNUMOBJECT = 0x1006; // GetNumObject opcode is 0x1006
    const WORD PTP_RESPONSECODE_OK = 0x2001;     // 0x2001 indicates command success

    // Build basic WPD parameters for the command
    CComPtr<IPortableDeviceValues> spParameters;
    if (hr == S_OK)
    {
        hr = CoCreateInstance(CLSID_PortableDeviceValues,
                              NULL,
                              CLSCTX_INPROC_SERVER,
                              IID_IPortableDeviceValues,
                              (VOID**)&spParameters);
    }

    // Use the WPD_COMMAND_MTP_EXT_EXECUTE_COMMAND_WITHOUT_DATA_PHASE command
    // Similar commands exist for reading and writing data phases
    if (hr == S_OK)
    {
        hr = spParameters->SetGuidValue(WPD_PROPERTY_COMMON_COMMAND_CATEGORY, 
                                           WPD_COMMAND_MTP_EXT_EXECUTE_COMMAND_WITHOUT_DATA_PHASE.fmtid);
    }

    if (hr == S_OK)
    {
        hr = spParameters->SetUnsignedIntegerValue(WPD_PROPERTY_COMMON_COMMAND_ID, 
                                                      WPD_COMMAND_MTP_EXT_EXECUTE_COMMAND_WITHOUT_DATA_PHASE.pid);
    }

    // Specify the actual MTP opcode that we want to execute here
    if (hr == S_OK)
    {
        hr = spParameters->SetUnsignedIntegerValue(WPD_PROPERTY_MTP_EXT_OPERATION_CODE, 
                                                      (ULONG) PTP_OPCODE_GETNUMOBJECT);
    }

    // GetNumObject requires three params - storage ID, object format, and parent object handle   
    // Parameters need to be first put into a PropVariantCollection
    CComPtr<IPortableDevicePropVariantCollection> spMtpParams;
    if (hr == S_OK)
    {
        hr = CoCreateInstance(CLSID_PortableDevicePropVariantCollection,
                                  NULL,
                                  CLSCTX_INPROC_SERVER,
                                  IID_IPortableDevicePropVariantCollection,
                                  (VOID**)&spMtpParams);
    }

    PROPVARIANT pvParam = {0};
    pvParam.vt = VT_UI4;

    // Specify storage ID parameter. Most devices that have 0x10001 have the storage ID. This
    // should be changed to use the device's real storage ID (which can be obtained by
    // removing the prefix for the WPD object ID for the storage)
    if (hr == S_OK)
    {
        pvParam.ulVal = 0x10001;
        hr = spMtpParams->Add(&pvParam);
    }

    // Specify object format code parameter. 0x0 can be specified to indicate this is unused 
    if (hr == S_OK)
    {
        pvParam.ulVal = 0x0;
        hr = spMtpParams->Add(&pvParam);
    }

    // Specify parent object handle parameter. 0x0 can be specified to indicate this is unused
    if (hr == S_OK)
    {
        pvParam.ulVal = 0x0;
        hr = spMtpParams->Add(&pvParam);
    }

    // Add MTP parameters collection to our main parameter list
    if (hr == S_OK)
    {
        hr = spParameters->SetIPortableDevicePropVariantCollectionValue(
                                          WPD_PROPERTY_MTP_EXT_OPERATION_PARAMS, spMtpParams);
    }  
```



After the parameters are set up, the application invokes the command.


```C++
// Send the command to the MTP device
    CComPtr<IPortableDeviceValues> spResults;
    if (hr == S_OK)
    {
        hr = pDevice->SendCommand(0, spParameters, &spResults);
    } 
```



After the application invokes the command, it processes the response from the MTP driver.


```C++
// Check if the driver was able to send the command by interrogating WPD_PROPERTY_COMMON_HRESULT
    HRESULT hrCmd = S_OK;
    if (hr == S_OK)
    {
         hr = spResults->GetErrorValue(WPD_PROPERTY_COMMON_HRESULT, &hrCmd);
    }

    if (hr == S_OK)
    {
        printf("Driver return code: 0x%08X\n", hrCmd);
        hr = hrCmd;
    }

    // If the command was executed successfully, check the MTP response code to see if the
    // device can handle the command. Be aware that there is a distinction between the command
    // being successfully sent to the device and the command being handled successfully by the device.
    DWORD dwResponseCode;
    if (hr == S_OK)
    {
        hr = spResults->GetUnsignedIntegerValue(WPD_PROPERTY_MTP_EXT_RESPONSE_CODE, &dwResponseCode);
    }

    if (hr == S_OK)
    {
        printf("MTP Response code: 0x%X\n", dwResponseCode);
        hr = (dwResponseCode == (DWORD) PTP_RESPONSECODE_OK) ? S_OK : E_FAIL;
    }
  
    // If the command was executed successfully, the MTP response parameters are returned in 
    // the WPD_PROPERTY_MTP_EXT_RESPONSE_PARAMS property, which is a PropVariantCollection
    CComPtr<IPortableDevicePropVariantCollection> spRespParams;
    if (hr == S_OK)
    {
        hr = spResults->GetIPortableDevicePropVariantCollectionValue(WPD_PROPERTY_MTP_EXT_RESPONSE_PARAMS, 
                                                                        &spRespParams);
    }

    // The first response parameter contains the number of objects result
    PROPVARIANT pvResult = {0};
    if (hr == S_OK)
    {
        hr = spRespParams->GetAt(0, &pvResult);
    }
   
    if (hr == S_OK)
    {
        printf("Reported number of objects: %d", pvResult.ulVal);
        PropVariantClear(&pvResult);    // Not really required, but use it for completeness
    }

    return hr;
}
```



## Related topics

<dl> <dt>

[Supporting MTP Extensions](supporting-mtp-extensions.md)
</dt> </dl>

 

 



