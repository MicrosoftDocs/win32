---
title: Sequence of Operations in the Tuning Process
description: Sequence of Operations in the Tuning Process
ms.assetid: 4b4f3fdd-536c-44b2-b5d6-6d89d1528b17
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Sequence of Operations in the Tuning Process

Tuning information is always contained in a tune request object. The application or the Video Control submits the tune request to the Network Provider. Tuning occurs in two general stages, locating and acquisition.

**Locating the Signal**

The Network Provider passes the tune request to the [BDA MPEG-2 Transport Information Filter](bda-mpeg-2-transport-information-filter.md) (TIF). The TIF fills in the information that the tuner needs to locate the signal, such as the carrier frequency. The tune request may or may not have a locator already attached to it. If not, the TIF creates the default locator for the tuning space. The TIF might update the locator with additional information, such as the TSID or network ID.

The Network Provider then tunes the BDA tuner to the correct frequency, and sets any other properties that are needed by the tuner, such as forward error correction (FEC) rates. The tuner passes the signal to the BDA capture filter, which digitizes the signal and delivers the MPEG-2 transport stream to the MPEG-2 Demultiplexer.

The TIF maps PID 0x00 to itself. PID 0x00 is reserved for the Program Association Table (PAT). As the TIF receives PAT sections, it notifies the Network Provider about which PIDs the PMTs and other tables are on. If the tune request is for another transport stream on the network, the Network Provider tunes the device again using the PMT information.

**Acquiring the Signal**

The Network Provider queries the TIF for the list of components in the program. It activates or deactivates particular components based on the preferred components list. It maps the corresponding PIDs on the demux, which then routes the streams to the correct output pins on the demux. The TIF continues to monitor the PMTs for service changes, and notifies the Network Provider if there are changes.

 

 




