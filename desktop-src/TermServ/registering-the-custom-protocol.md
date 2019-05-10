---
title: Registering the Protocol Manager
description: You must create at least one registry value entry for your protocol manager so that the Remote Desktop Services service can instantiate it.
ms.assetid: 4cc7197b-88f3-4906-9b59-66587f970e2a
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Registering the Protocol Manager

You must create at least one registry value entry for your protocol manager so that the Remote Desktop Services service can instantiate it.

## Registry Location

Create a registry key in the following location for each listener ([**IWRdsProtocolListener**](/windows/desktop/api/wtsprotocol/nn-wtsprotocol-iwrdsprotocollistener)) that your protocol uses. In this example, the new listener keys are called *MyListener1* and *MyListener2*.

```
HKEY_LOCAL_MACHINE
   System
      CurrentControlSet
         Control
            Terminal Server
               WinStations
                  RDP-Tcp
                  MyListener1
                  MyListener2
```

For reference, you can view the value entries under the default **RDP-Tcp** listener key in this location.

## Registry Value Entries

The listener key for the protocol must have a value entry called **LoadableProtocol\_Object**<dl> <dt>

Data type
</dt> <dd>REG_SZ</dd> </dl> of type **REG\_SZ** that contains the CLSID of the protocol manager for that listener. (The protocol manager is a COM server that implements the <a href="/windows/desktop/api/wtsprotocol/nn-wtsprotocol-iwrdsprotocolmanager">**IWRdsProtocolManager**</a> interface.) The Remote Desktop Services service uses this CLSID to instantiate the protocol manager for this listener after it finds the listener in the registry.

If your protocol provider uses more than one listener, the Remote Desktop Services service only creates one instance of the protocol manager, and uses it to call [**CreateListener**](/windows/desktop/api/wtsprotocol/nf-wtsprotocol-iwrdsprotocolmanager-createlistener) once for each listener.

## Related topics

<dl> <dt>

[Creating a Remote Desktop Protocol Provider](creating-a-custom-remote-protocol.md)
</dt> <dt>

[Method Call Sequence](method-call-sequence.md)
</dt> </dl>

 

 




