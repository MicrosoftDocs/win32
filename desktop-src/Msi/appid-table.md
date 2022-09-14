---
description: The AppId table or the Registry table specifies that the installer configure and register DCOM servers to do one of the following during an installation.
ms.assetid: d76ed6df-944b-4996-bf07-e42ceb7a1b69
title: AppId Table
ms.topic: article
ms.date: 05/31/2018
---

# AppId Table

The AppId table or the [Registry table](registry-table.md) specifies that the installer configure and register DCOM servers to do one of the following during an installation.

-   Run the DCOM server under a different identity than the user activating the server. For example, to configure a DCOM server to always run as an interactive user or as a predefined user.
-   Run the DCOM server as a service.
-   Configure the default security access for the DCOM server.
-   Register the DCOM server such that it is activated on a different computer.

This table is processed at the installation of the component associated with the DCOM server in the \_Component column of the [Class table](class-table.md). An AppId is not advertised.

The AppId table has the following columns.



| Column               | Type                       | Key | Nullable |
|----------------------|----------------------------|-----|----------|
| AppId                | [GUID](guid.md)           | Y   | N        |
| RemoteServerName     | [Formatted](formatted.md) | N   | Y        |
| LocalService         | [Text](text.md)           | N   | Y        |
| ServiceParameters    | [Text](text.md)           | N   | Y        |
| DllSurrogate         | [Text](text.md)           | N   | Y        |
| ActivateAtStorage    | [Integer](integer.md)     | N   | Y        |
| RunAsInteractiveUser | [Integer](integer.md)     | N   | Y        |



 

## Columns

<dl> <dt>

<span id="AppId"></span><span id="appid"></span><span id="APPID"></span>AppId
</dt> <dd>

The AppId column of the [Class table](class-table.md) is a foreign key into this column of the AppId table. This column contains the AppId value that will be written under the CLSID and creates the AppId GUID key under HKCR\\AppId.

</dd> <dt>

<span id="RemoteServerName"></span><span id="remoteservername"></span><span id="REMOTESERVERNAME"></span>RemoteServerName
</dt> <dd>

This column contains the value of "RemoteServerName"=&lt;xxxx&gt; that will be written under HKCR\\AppID\\{AppID}\\ .

</dd> <dt>

<span id="LocalService"></span><span id="localservice"></span><span id="LOCALSERVICE"></span>LocalService
</dt> <dd>

This column contains the value of LocalService that will be written under HKCR\\AppID\\{&lt;appid&gt;} "LocalService"=&lt;xxx&gt;.

</dd> <dt>

<span id="ServiceParameters"></span><span id="serviceparameters"></span><span id="SERVICEPARAMETERS"></span>ServiceParameters
</dt> <dd>

This column contains the value of ServiceParameters that will be written under HKCR\\AppID\\{appid>} "ServiceParameters".

</dd> <dt>

<span id="DllSurrogate"></span><span id="dllsurrogate"></span><span id="DLLSURROGATE"></span>DllSurrogate
</dt> <dd>

This column contains the value of DllSurrogate that will be written under HKCR\\AppId\\{&lt;appid&gt;} "DllSurrogate"=&lt;xxx&gt;. If this column is present it will typically be an empty string.

</dd> <dt>

<span id="ActivateAtStorage"></span><span id="activateatstorage"></span><span id="ACTIVATEATSTORAGE"></span>ActivateAtStorage
</dt> <dd>

A non-zero integer value in this field causes Windows Installer to write HKCR\\AppID\\{&lt;appid&gt;} "ActivateAtStorage"="Y" into the registry. If the field is left empty, or has a value of zero, no value will be written.

</dd> <dt>

<span id="RunAsInteractiveUser"></span><span id="runasinteractiveuser"></span><span id="RUNASINTERACTIVEUSER"></span>RunAsInteractiveUser
</dt> <dd>

A non-zero integer value in this field causes Windows Installer to write HKCR\\AppID\\{appid>} "RunAs"="Interactive User" into the registry. If the field is left empty, or has a value of zero, no value will be written.

</dd> </dl>

## Remarks

This table is used by the [RegisterClassInfo action](registerclassinfo-action.md) and [UnregisterClassInfo action](unregisterclassinfo-action.md).

Note that the AppId table does not have a column for registering a Default name. Therefore in cases where you need to write a user friendly name as the Default name value, you must register using the [Registry table](registry-table.md).

## Validation

<dl>

[ICE03](ice03.md)  
[ICE06](ice06.md)  
[ICE32](ice32.md)  
[ICE33](ice33.md)  
[ICE46](ice46.md)  
[ICE69](ice69.md)  
</dl>

 

 



