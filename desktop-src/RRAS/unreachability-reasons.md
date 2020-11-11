---
title: Unreachability Reasons
description: The following table lists constant values that indicate why an interface is unreachable.
ms.assetid: 55c0519e-02c8-4a04-bed9-9fe94327a4b6
ms.topic: article
ms.date: 05/31/2018
---

# Unreachability Reasons

The following table lists constant values that indicate why an interface is unreachable.



| Value                                       | Meaning                                                                                        |
|---------------------------------------------|------------------------------------------------------------------------------------------------|
| MPR\_INTERFACE\_ADMIN\_DISABLED             | The administrator has disabled the interface.                                                  |
| MPR\_INTERFACE\_CONNECTION\_FAILURE         | The previous connection attempt failed. Look at the **dwLastError** member for the error code. |
| MPR\_INTERFACE\_DIALOUT\_HOURS\_RESTRICTION | Dial-out is not allowed at the current time.                                                   |
| MPR\_INTERFACE\_OUT\_OF\_RESOURCES          | No ports or devices are available for use.                                                     |
| MPR\_INTERFACE\_SERVICE\_PAUSED             | The service is paused.                                                                         |
| MPR\_INTERFACE\_NO\_MEDIA\_SENSE            | The network cable is disconnected from the network card.                                       |
| MPR\_INTERFACE\_NO\_DEVICE                  | The network card has been removed from the machine.                                            |



 

## Related topics

<dl> <dt>

[**MPR\_INTERFACE\_0**](/windows/desktop/api/Mprapi/ns-mprapi-mpr_interface_0)
</dt> <dt>

[**MPR\_INTERFACE\_1**](/windows/desktop/api/Mprapi/ns-mprapi-mpr_interface_1)
</dt> <dt>

[**MIB\_IFROW**](/windows/desktop/api/ifmib/ns-ifmib-mib_ifrow)
</dt> <dt>

[**MIB\_IFSTATUS**](/windows/desktop/api/iprtrmib/ns-iprtrmib-mib_ifstatus)
</dt> </dl>

 

 