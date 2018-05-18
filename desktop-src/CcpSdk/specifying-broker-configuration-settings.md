---
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '1b574dc8-1da4-4ee4-9658-8fdf05fca7ab'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: Specifying Broker Configuration Settings
---

# Specifying Broker Configuration Settings

You can use the following options to specifying the broker configuration settings:

-   Use the [SessionStartInfo.BrokerSettingsInfo](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.session.sessionstartinfo.brokersettingsinfo.aspx) class to specify the settings that control the broker's behavior for this session (overrides a subset of the broker settings).
-   Modify the settings in the %CCP\_HOME%Bin\\HpcWcfBroker.exe.config configuration file. The configuration file contains the global broker settings that all HPC brokers that run on the broker node will use.
-   Create a broker configuration file for your service.

To create a broker configuration file for your service, perform the following steps:

1.  Copy %CCP\_HOME%Bin\\HpcWcfBroker.exe to %CCP\_HOME%Bin\\*servicename*HpcWcfBroker.exe, where *servicename* is the name of your service. For example, if the name of your service is AsianOptions, copy %CCP\_HOME%Bin\\HpcWcfBroker.exe to %CCP\_HOME%Bin\\AsianOptionsHpcWcfBroker.exe.
2.  Run the following command:

    **cluscfg setparams AsianOptions.BrokerTaskProgram="%ccp\_home%bin\\AsianOptionsHpcWcfBroker.exe**

3.  Copy %CCP\_HOME%Bin\\HpcWcfBroker.exe.config to %CCP\_HOME%Bin\\AsianOptionsHpcWcfBroker.exe.config.
4.  Modify the settings of %CCP\_HOME%Bin\\AsianOptionsHpcWcfBroker.exe.config as appropriate for your service. Typically, you change the client binding that the broker uses to talk to the backend services.

 

 



