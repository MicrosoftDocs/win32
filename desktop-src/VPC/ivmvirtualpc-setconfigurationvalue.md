---
title: IVMVirtualPC SetConfigurationValue method (VPCCOMInterfaces.h)
description: Sets the value of the specified configuration setting.
ms.assetid: 7760b81e-734d-4970-8875-f2d310ff6c5c
keywords:
- SetConfigurationValue method Virtual PC
- SetConfigurationValue method Virtual PC , IVMVirtualPC interface
- IVMVirtualPC interface Virtual PC , SetConfigurationValue method
topic_type:
- apiref
api_name:
- IVMVirtualPC.SetConfigurationValue
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMVirtualPC::SetConfigurationValue method

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Sets the value of the specified configuration setting.

## Syntax


```C++
HRESULT SetConfigurationValue(
  [in] BSTR    preferenceKey,
  [in] VARIANT preferenceValue
);
```



## Parameters

<dl> <dt>

*preferenceKey* \[in\]
</dt> <dd>

The key used to identify the preference, as stored in the per-user configuration file (Options.xml in "%LocalAppData%\\Microsoft\\Windows Virtual PC").

> [!IMPORTANT]
> Changes should be made to Options.xml only using the **SetConfigurationValue** method. Changing Options.xml using any other method is not supported.

 

</dd> <dt>

*preferenceValue* \[in\]
</dt> <dd>

The preference value. This value may be one of the following **VARIANT** types: **VT\_ARRAY**\|**VT\_UI1** (raw bytes), **VT\_BSTR** (string), **VT\_UI4** (integer), or **VT\_BOOL** (Boolean).

</dd> </dl>

## Return value

This method can return one of these values.



| Return code/value                                                                                                                                                                        | Description                                                                                     |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> <dt>0</dt> </dl>                                              | The operation was successful.<br/>                                                        |
| <dl> <dt>**E\_POINTER**</dt> <dt>0x80004003</dt> </dl>                                | The *preferenceKey* or *preferenceValue* parameter is **NULL**.<br/>                      |
| <dl> <dt>**E\_INVALIDARG**</dt> <dt>0x80000003</dt> </dl>                             | The *preferenceKey* parameter is not valid or is an empty string.<br/>                    |
| <dl> <dt>**DISP\_E\_EXCEPTION**</dt> <dt>0x80020009</dt> </dl>                        | An unexpected error has occurred.<br/>                                                    |
| <dl> <dt>**E\_ACCESSDENIED**</dt> <dt>0x80070005</dt> </dl>                           | The current user has insufficient access to the configuration file.<br/>                  |
| <dl> <dt>**VM\_E\_HARDWARE\_VIRTUALIZATION\_DISABLED**</dt> <dt>0xA0040951</dt> </dl> | The processor does not support Hardware Accelerated Virtualization (HAV) extensions.<br/> |



 

## Remarks

The following values are supported for the *preferenceKey* parameter.



| *preferenceKey* value      | Description                                                                                                                                                                           | Data type            | Default value   |
|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------|-----------------|
| "idle\_timeout"<br/> | Number of seconds that vpc.exe should wait before exiting if there are no active VMs or applications using the [Windows Virtual PC Interfaces](virtual-pc-interfaces.md).<br/> | "integer"<br/> | "30"<br/> |



 

This method provides low-level access to any configuration value. It can be used to set configuration values for customer-defined keys. Be careful if you use this method to set system configuration values, because no error checking is performed on the configuration value. Also, some configuration values cannot be changed while a virtual machine is running.

Configuration keys are located in the virtual machine's "Options.xml" file in XML format. The keys are stored in a hierarchical manner similar to the registry keys in Windows. To specify a specific subkey, a "key path" is constructed which specifies the various keys in a slash mark delimited format.

For example, to set the value of the "idle\_timeout" key located in the following key tree:

``` syntax
<preferences>
  <idle_timeout type="integer">60</idle_timeout>
```

The *preferenceKey* path string would be specified as follows:

``` syntax
"idle_timeout"
```

If any of the keys in the desired tree have an "id" attribute value, the attribute and its value is embedded in the *preferenceKey* path string immediately after its associated configuration key using the following bracketed format: "\[@id="*id\_value*"\]".

For example, to set the value of the "golf" key located in the following key tree:

``` syntax
<preferences>
  <alpha>
    <bravo>
      <charlie>
        <delta id="1">
          <echo id="0">
            <foxtrot>
              <golf type="string">D</golf>
```

The *preferenceKey* path string would be specified as follows:

``` syntax
"alpha/bravo/charlie/delta[@id=1]/echo[@id=0]/foxtrot/golf"
```

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | None supported<br/>                                                                     |
| End of client support<br/>    | Windows 7<br/>                                                                          |
| Product<br/>                  | Windows Virtual PC<br/>                                                                 |
| Header<br/>                   | <dl> <dt>VPCCOMInterfaces.h</dt> </dl> |
| IID<br/>                      | IID\_IVMVirtualPC is defined as 236ba0d9-a24a-4292-a132-27c1421dfd01<br/>               |



## See also

<dl> <dt>

[**IVMVirtualPC**](ivmvirtualpc.md)
</dt> <dt>

[**IVMVirtualMachine::SetConfigurationValue**](ivmvirtualmachine-setconfigurationvalue.md)
</dt> </dl>

 

