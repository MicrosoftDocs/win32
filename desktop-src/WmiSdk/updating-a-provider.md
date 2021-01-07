---
description: Sometimes you may need to install a newer version of a provider onto a running system.
ms.assetid: 44c4c16a-fd79-483a-81ef-a0f74a2cdf45
ms.tgt_platform: multiple
title: Updating a Provider
ms.topic: article
ms.date: 05/31/2018
---

# Updating a Provider

Sometimes you may need to install a newer version of a provider onto a running system. If your provider is installed as a DLL, you can install a new provider without having to restart the service, reboot the computer, or otherwise affect any applications using WMI at that time.

The following procedure describes how to update a provider.

**To update a provider**

1.  Build the new provider.

    1.  Compile the new provider with a different DLL name and a different **CLSID**.

        For example, change Myprov.dll to Myprov1.dll, and **CLSID\_MyProProv** to **CLSID\_MyProv**1.

    2.  Modify the provider registration MOF file to use the new CLSID (CLSID\_MyProv1), but the same provider name ("MyProv").

2.  Install the new provider.

    1.  Copy the new provider DLL with the new name alongside the old one.
    2.  Self-register the new provider.

        For example, use the **regsvr32** **myprov1.dll** command to register the new provider.

    3.  Compile the new provider registration MOF, thus overwriting the old provider registration. Until this point, the old provider was fully functional; now the new provider is fully operational.

3.  Remove the old version of the provider, if necessary.

    1.  Unregister the old DLL.

        For example, use the **regsvr32** **/umyprov.dll** command to unregister the old DLL.

    2.  Mark the old DLL to be deleted on reboot by calling [**MoveFileEx**](/windows/desktop/api/winbase/nf-winbase-movefileexa).

You can take similar steps to upgrade a local server-implemented provider.

## Related topics

<dl> <dt>

[Developing a WMI Provider](developing-a-wmi-provider.md)
</dt> <dt>

[Setting Namepace Security Descriptors](setting-namespace-security-descriptors.md)
</dt> <dt>

[Securing Your Provider](securing-your-provider.md)
</dt> </dl>

 

 
