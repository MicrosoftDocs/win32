---
description: The global flags constants are used to enable or disable user power policy options.
ms.assetid: d98190ef-f70e-4796-960e-ff32d2cf6f4f
title: Global Flags Constants (PowrProf.h)
ms.topic: reference
ms.date: 05/31/2018
---

# Global Flags Constants

The global flags constants are used to enable or disable user power policy options.



| Constant/value                                                                                                                                                                                                                                                                                         | Description                                                                                                                                        |
|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="EnableMultiBatteryDisplay"></span><span id="enablemultibatterydisplay"></span><span id="ENABLEMULTIBATTERYDISPLAY"></span><dl> <dt>**EnableMultiBatteryDisplay**</dt> <dt>0x02</dt> </dl> | Enables or disables multiple battery display in the system Power Meter.<br/>                                                                 |
| <span id="EnablePasswordLogon"></span><span id="enablepasswordlogon"></span><span id="ENABLEPASSWORDLOGON"></span><dl> <dt>**EnablePasswordLogon**</dt> <dt>0x04</dt> </dl>                         | Enables or disables requiring password logon when the system resumes from standby or hibernate.<br/>                                         |
| <span id="EnableSysTrayBatteryMeter"></span><span id="enablesystraybatterymeter"></span><span id="ENABLESYSTRAYBATTERYMETER"></span><dl> <dt>**EnableSysTrayBatteryMeter**</dt> <dt>0x01</dt> </dl> | Enables or disables the battery meter icon in the system tray. When this flag is cleared, the battery meter icon is not displayed.<br/>      |
| <span id="EnableVideoDimDisplay"></span><span id="enablevideodimdisplay"></span><span id="ENABLEVIDEODIMDISPLAY"></span><dl> <dt>**EnableVideoDimDisplay**</dt> <dt>0x10</dt> </dl>                 | Enables or disables support for dimming the video display when the system changes from running on AC power to running on battery power.<br/> |
| <span id="EnableWakeOnRing"></span><span id="enablewakeonring"></span><span id="ENABLEWAKEONRING"></span><dl> <dt>**EnableWakeOnRing**</dt> <dt>0x08</dt> </dl>                                     | Enables or disables wake on ring support.<br/>                                                                                               |



## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>PowrProf.h</dt> </dl> |



## See also

<dl> <dt>

[**GLOBAL\_USER\_POWER\_POLICY**](/windows/desktop/api/PowrProf/ns-powrprof-global_user_power_policy)
</dt> </dl>

 

 




