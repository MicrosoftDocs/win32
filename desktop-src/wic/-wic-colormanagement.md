---
Description: 'Windows Imaging Component (WIC) simplifies color management by providing the IWICColorContext interface and the IWICColorTransform interface.'
ms.assetid: 'd4d761a6-d5a6-47b8-b655-7651bd415e4e'
title: Color Management Overview
---

# Color Management Overview

Digital images originate from and are targeted at a variety of devices, each of which has its own gamut and dynamic range. If a photographer were to capture the same scene on two different cameras, the colors in the resulting images would not appear exactly the same, even when rendered on the same output device because the color gamut capabilities of the two source devices were different. Likewise, the same image rendered on two different target devices will appear differently because the target devices have different color profiles. To ensure consistent color reproduction across devices, it's necessary to create a mapping from the color profile of the source device to the color profile of the target device. Color management seeks to produce a close and consistent visual match and is a critical feature in professional imaging.

Being able to consistently reproduce color across scanners, monitors, printers, and applications sounds like a simple goal, but without a color management system in the operating system, it's difficult to achieve. If each application is required to generate its own color profiles, it's almost impossible to achieve consistent color interchange throughout the publishing process, which includes scanning, editing and composition, proofing, and distribution.

Windows Imaging Component (WIC) simplifies color management by providing the [**IWICColorContext**](-wic-codec-iwiccolorcontext.md) interface and the [**IWICColorTransform**](-wic-codec-iwiccolortransform.md) interface.You can get an [**IWICColorTransform**](-wic-codec-iwiccolortransform.md) object using the [**IWICFactory::CreateColorTransformer**](-wic-codec-iwicimagingfactory-createcolortransformer.md). The [**IWICColorContext**](-wic-codec-iwiccolorcontext.md) is an abstraction for device color profile. **IWICColorContext** is initialized with a bitmap frame, the color profile of the source device and the color profile of the target device. It performs the conversion of the bitmap frame.

 

 



