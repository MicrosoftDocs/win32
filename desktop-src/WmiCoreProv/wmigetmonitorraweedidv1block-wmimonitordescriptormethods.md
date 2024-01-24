---
description: Gets the raw data for a specified Video Electronics Standard Association (VESA) Enhanced Extended Display Identification Data (E-EDID) structure that defines optimal settings for configuring a monitor.
ms.assetid: a787e66e-1b96-4dd5-8646-7aa2d281ac95
title: WmiGetMonitorRawEEdidV1Block method of the WmiMonitorDescriptorMethods class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- WmiMonitorDescriptorMethods.WmiGetMonitorRawEEdidV1Block
api_type: 
- COM
api_location: 
- WmiProv.dll
---

# WmiGetMonitorRawEEdidV1Block method of the WmiMonitorDescriptorMethods class

The **WmiGetMonitorRawEEdidV1Block** method gets the raw data for a specified Video Electronics Standard Association (VESA) Enhanced Extended Display Identification Data (E-EDID) structure that defines optimal settings for configuring a monitor.

## Syntax


```mof
uint32 WmiGetMonitorRawEEdidV1Block(
  [in]  uint8 BlockId,
  [out] uint8 BlockType,
  [out] uint8 BlockContent[]
);
```



## Parameters

<dl> <dt>

*BlockId* \[in\]
</dt> <dd>

The data block identity.

</dd> <dt>

*BlockType* \[out\]
</dt> <dd>

Type of data block. The following table lists possible return values.



| Value                                                                                 | Meaning                    |
|---------------------------------------------------------------------------------------|----------------------------|
| <dl> <dt>0 (0x0)</dt> </dl>    | Uninitialized<br/>   |
| <dl> <dt>1 (0x1)</dt> </dl>    | EDID base block<br/> |
| <dl> <dt>2 (0x2)</dt> </dl>    | EDID block map<br/>  |
| <dl> <dt>255 (0xFF)</dt> </dl> | Other<br/>           |



 

</dd> <dt>

*BlockContent* \[out\]
</dt> <dd>

A 128-byte array that contains the raw block content.

</dd> </dl>

## Return value

Returns zero (0) to indicate success. Any other number indicates an error. For more information about error codes, see [**WMI Error Constants**](/windows/desktop/WmiSdk/wmi-error-constants) or [**WbemErrorEnum**](/windows/desktop/api/wbemdisp/ne-wbemdisp-wbemerrorenum).

## Examples

The following code example retrieves the EDID blocks of any display as raw 128 bit arrays.


```CSharp
static void Main(string[] args)
{
    ManagementClass mc = new ManagementClass(string.Format(@"\\{0}\root\wmi:WmiMonitorDescriptorMethods", Environment.MachineName));


    foreach (ManagementObject mo in mc.GetInstances()) //Do this for each connected monitor
    {              


        for (int i = 0; i < 256; i++)
        {
            ManagementBaseObject inParams = mo.GetMethodParameters("WmiGetMonitorRawEEdidV1Block");
            inParams["BlockId"] = i; 


            ManagementBaseObject outParams = null;
            try
            {
                outParams = mo.InvokeMethod("WmiGetMonitorRawEEdidV1Block", inParams, null);
                Console.Out.WriteLine("Returned a block of type {0}, having a content of type {1} ",
                                  outParams["BlockType"], outParams["BlockContent"].GetType());
            }
            catch { break; } //No more EDID blocks


                    
        }
    }
}
```



## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Namespace<br/>                | Root\\wmi<br/>                                                                   |
| MOF<br/>                      | <dl> <dt>WmiCore.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WmiProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**WmiMonitorDescriptorMethods**](wmimonitordescriptormethods.md)
</dt> <dt>

[**MSMonitorClass**](msmonitorclass.md)
</dt> </dl>

 

