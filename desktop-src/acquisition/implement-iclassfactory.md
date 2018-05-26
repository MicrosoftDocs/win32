---
Description: Implement IClassFactory
ms.assetid: f0d1c4f0-068c-4405-89d2-a21e1664320c
title: Implement IClassFactory
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Implement IClassFactory

Your plug-in must define a class that implements the [IClassFactory](https://msdn.microsoft.com/library/windows/desktop/ms694364) interface. Your implementation of [IClassFactory::CreateInstance](https://msdn.microsoft.com/library/windows/desktop/ms682215) should call your implementation of [**IPhotoAcquirePlugin::Initialize**](/windows/win32/PhotoAcquire/nf-photoacquire-iphotoacquireplugin-initialize?branch=master).

 

 



