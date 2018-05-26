---
title: Video Control Interface Hierarchy
description: Video Control Interface Hierarchy
ms.assetid: c8956366-1c55-463c-860b-6e8a2f7ec4eb
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Video Control Interface Hierarchy

This topic applies to Windows XP or later.

Tuners, renderers, and features expose a variety of interfaces, all of which ultimately derive from the [**IMSVidDevice**](/windows/win32/segment/nn-segment-imsviddevice?branch=master) interface. The following diagram shows the inheritance hierarchy for the devices and features that are currently supported.

![video control interface hierarchy](images/mstv-vc-objects.gif)

The shaded interfaces are not directly exposed by any objects. They act as base interfaces, to support polymorphism. For example, the [**IMSVidCtl::get\_InputActive**](/windows/previous-versions/msvidctl/nf-msvidctl-imsvidctl-get_inputactive?branch=master) method returns an [**IMSVidInputDevice**](/windows/win32/segment/nn-segment-imsvidinputdevice?branch=master) pointer. The returned object might be a digital tuner that exposes [**IMSVidTuner**](/windows/win32/segment/nn-segment-imsvidtuner?branch=master), or an analog tuner that exposes [**IMSVidAnalogTuner**](/windows/win32/segment/nn-segment-imsvidanalogtuner?branch=master). You can query the returned pointer to learn more about the object.

 

 




