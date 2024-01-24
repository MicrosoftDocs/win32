---
title: IVMVirtualMachine SetConfigurationValue method (VPCCOMInterfaces.h)
description: Sets the value of the specified configuration setting for this virtual machine (VM).
ms.assetid: 43c3ac88-2e25-4c9e-a2ac-fcae5add62c5
keywords:
- SetConfigurationValue method Virtual PC
- SetConfigurationValue method Virtual PC , IVMVirtualMachine interface
- IVMVirtualMachine interface Virtual PC , SetConfigurationValue method
topic_type:
- apiref
api_name:
- IVMVirtualMachine.SetConfigurationValue
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMVirtualMachine::SetConfigurationValue method

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Sets the value of the specified configuration setting for this virtual machine (VM).

## Syntax


```C++
HRESULT SetConfigurationValue(
  [in] BSTR    configurationKey,
  [in] VARIANT configurationValue
);
```



## Parameters

<dl> <dt>

*configurationKey* \[in\]
</dt> <dd>

The key used to identify the configuration value as stored in the "\*.vmc" file.

> [!IMPORTANT]
> Changes should be made to "\*.vmc" only using the **SetConfigurationValue** method. Changing "\*.vmc" using any other method is not supported.

 

</dd> <dt>

*configurationValue* \[in\]
</dt> <dd>

The configuration value. This value cay be one of the following **VARIANT** types: **VT\_ARRAY**\|**VT\_UI1** (raw bytes), **VT\_BSTR** (string), **VT\_UI4** (integer), or **VT\_BOOL** (Boolean).

</dd> </dl>

## Return value

This method can return one of these values.



| Return code/value                                                                                                                                                 | Description                                                                                                                         |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> <dt>0</dt> </dl>                       | The operation was successful.<br/>                                                                                            |
| <dl> <dt>**E\_INVALIDARG**</dt> <dt>0x80000003</dt> </dl>      | The *configurationKey* parameter is **NULL** or empty or the *configurationValue* parameter is not a valid variant type.<br/> |
| <dl> <dt>**VM\_E\_VM\_UNKNOWN**</dt> <dt>0xA0040207</dt> </dl> | The configuration is unknown.<br/>                                                                                            |
| <dl> <dt>**DISP\_E\_EXCEPTION**</dt> <dt>0x80020009</dt> </dl> | An unexpected error has occurred.<br/>                                                                                        |



 

## Remarks

The following values are supported for the *configurationKey* parameter.



| *configurationKey* value                                     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Data type            | Default value     |
|--------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------|-------------------|
| "hardware/bios/time\_sync\_at\_boot"<br/>              | "true" if the VM CMOS clock is to be synchronized with the host clock at boot; "false" otherwise.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | "boolean"<br/> | "true"<br/> |
| "integration/microsoft/host\_time\_sync/enabled""<br/> | "true" if host time synchronization is enabled in the integration components; "false" otherwise.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | "boolean"<br/> | "true"<br/> |
| "ui\_options/auto\_app\_publish"<br/>                  | "true" if automatic publishing of applications is enabled in the integration components; "false" otherwise. This is also called virtual applications.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | "boolean"<br/> | "true"<br/> |
| "ui\_options/seconds\_to\_save"<br/>                   | Number of seconds to wait before saving the VM after all applications are closed. However, values below 20 and more than 4,294,968 have special meanings. For details, see the following list<br/> <dl> <dt><span id="0"></span>0</dt> <dd> Never save the VM.<br/> </dd> <dt><span id="120"></span>1 20</dt> <dd> Wait 20 seconds before saving the VM.<br/> </dd> <dt><span id="214_294_967"></span>21 4,294,967</dt> <dd> Wait the specified number of seconds before saving the VM.<br/> </dd> <dt><span id="4_294_9684_294_967_295"></span>4,294,968 4,294,967,295</dt> <dd> Wait 4,294,968 seconds before saving the VM.<br/> </dd> </dl> | "integer"<br/> | 300<br/>    |



 

This method provides low-level access to any configuration value. It can be used to set configuration values for customer-defined keys. Be careful if you use this method to set system configuration values, because no error checking is performed on the configuration value. Also, some configuration values cannot be changed while the virtual machine is running.

Configuration keys are located in the virtual machine's "\*.vmc" file in XML format. The keys are stored in a hierarchical manner similar to the registry keys in Windows. To specify a specific subkey, a "key path" is constructed which specifies the various keys in a slash mark delimited format.

For example, to set the value of the "ram\_size" key located in the following key tree:

``` syntax
<preferences>
  <hardware>
    <bios>
      <time_sync_at_boot type="boolean">true</time_sync_at_boot>
```

The *configurationKey* path string would be specified as follows:

``` syntax
"hardware/memory/ram_size"
```

If any of the keys in the desired tree have an "id" attribute value, the attribute and its value is embedded in the *configurationKey* path string immediately after its associated configuration key using the following bracketed format: "\[@id="*id\_value*"\]".

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

The *configurationKey* path string would be specified as follows:

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
| IID<br/>                      | IID\_IVMVirtualMachine is defined as f7092aa1-33ed-4f78-a59f-c00adfc2edd7<br/>          |



## See also

<dl> <dt>

[**IVMVirtualMachine**](ivmvirtualmachine.md)
</dt> <dt>

[**IVMVirtualPC::SetConfigurationValue**](ivmvirtualpc-setconfigurationvalue.md)
</dt> </dl>

 

