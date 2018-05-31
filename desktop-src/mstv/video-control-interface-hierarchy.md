---
title: Video Control Interface Hierarchy
description: Video Control Interface Hierarchy
ms.assetid: c8956366-1c55-463c-860b-6e8a2f7ec4eb
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Video Control Interface Hierarchy

This topic applies to Windows XP or later.

Tuners, renderers, and features expose a variety of interfaces, all of which ultimately derive from the [**IMSVidDevice**](/windows/desktop/api/segment/nn-segment-imsviddevice) interface. The following diagram shows the inheritance hierarchy for the devices and features that are currently supported.

![video control interface hierarchy](images/mstv-vc-objects.gif)

The shaded interfaces are not directly exposed by any objects. They act as base interfaces, to support polymorphism. For example, the [**IMSVidCtl::get\_InputActive**](/previous-versions/windows/desktop/api/msvidctl/nf-msvidctl-imsvidctl-get_inputactive) method returns an [**IMSVidInputDevice**](/windows/desktop/api/segment/nn-segment-imsvidinputdevice) pointer. The returned object might be a digital tuner that exposes [**IMSVidTuner**](/windows/desktop/api/segment/nn-segment-imsvidtuner), or an analog tuner that exposes [**IMSVidAnalogTuner**](/windows/desktop/api/segment/nn-segment-imsvidanalogtuner). You can query the returned pointer to learn more about the object.

 

 




