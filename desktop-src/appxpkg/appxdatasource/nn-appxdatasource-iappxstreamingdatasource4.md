---
UID: NN:appxdatasource.IAppxStreamingDataSource4
title: IAppxStreamingDataSource4
description: Provides access to a data source. Deployment will query for this interface on the data source returned by the data source factory.
ms.topic: reference
tech.root: appxpkg
ms.date: 02/08/2024
targetos: Windows
prerelease: false
req.assembly: 
req.construct-type: iface
req.ddi-compliance: 
req.header: 
req.idl: 
req.include-header: 
req.max-support: 
req.namespace: 
req.redist: 
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.target-type: 
req.unicode-ansi: 
topic_type:
 - apiref
api_type:
 - COM
api_location:
 - AppxStreamingDataSourcePS.dll
api_name:
 - IAppxStreamingDataSource4
f1_keywords:
 - IAppxStreamingDataSource4
 - appxdatasource/IAppxStreamingDataSource4
dev_langs:
 - c++
helpviewer_keywords:
 - IAppxStreamingDataSource4
---

# IAppxStreamingDataSource4 interface

Provides access to a data source. Deployment will query for this interface on the data source returned by the data source factory. Upon success, deployment will request the MSIXVC (Microsoft Installer for Xbox Virtual Console) manifest. An MSIXVC data source is expected to implement this interface. It's expected that `appxsvc` can access all of the files referenced in the manifest (for example, visual assets) during the appropriate steps of the install process (for example, tile registration).

## Inheritance

The **IAppxStreamingDataSource4** interface derives from the **IUnknown** interface.

## Methods

The **IAppxStreamingDataSource4** interface has these methods.

| &nbsp; |
| ---- |
| [Apply](../appxdatasource/nf-appxdatasource-iappxstreamingdatasource4-apply.md) <br><br> Applies an update from an outdated package to an updating package. |
| [GetDiskSpace](../appxdatasource/nf-appxdatasource-iappxstreamingdatasource4-getdiskspace.md) <br><br> Retrieves a value representing the total disk space used by the package. |
| [GetManifestStream](../appxdatasource/nf-appxdatasource-iappxstreamingdatasource4-getmanifeststream.md) <br><br> Retrieves the appx manifest stream of an MSIXVC package. |
| [GetSignatureFileStream](../appxdatasource/nf-appxdatasource-iappxstreamingdatasource4-getsignaturefilestream.md) <br><br> Retrieves the signature file stream of an MSIXVC package. |
| [GetTotalSize](../appxdatasource/nf-appxdatasource-iappxstreamingdatasource4-gettotalsize.md) <br><br> Returns the total download size of the MSIXVC package. |
| [Move](../appxdatasource/nf-appxdatasource-iappxstreamingdatasource4-move.md) <br><br> Moves the package from the current volume to another. |
| [Pause](../appxdatasource/nf-appxdatasource-iappxstreamingdatasource4-pause.md) <br><br> Terminates the request, causing the corresponding Run call to return E_ABORT. |
| [Remove](../appxdatasource/nf-appxdatasource-iappxstreamingdatasource4-remove.md) <br><br> Cancels any outstanding Run calls (causing them to return), and removes the package contents. |
| [Run](../appxdatasource/nf-appxdatasource-iappxstreamingdatasource4-run.md) <br><br> Initiates the streaming operation (request). |

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **DLL** | AppxStreamingDataSourcePS.dll |
