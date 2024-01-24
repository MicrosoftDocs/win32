---
title: Desktop Win32 code samples
description: About the samples repos for Win32, and how to search in them.
ms.topic: article
ms.date: 03/19/2021
---

# Desktop Win32 code samples

Also see [Code samples](https://developer.microsoft.com/windows/samples/).

## Find a sample for the API you're interested in

You can use Microsoft Visual Studio to search an entire repo's source code to see whether the usage of a particular Windows API is being demonstrated.

* Clone any of the repos listed in the sections below (or download the ZIP) to your local file system.
* Then **Find in Files** in Visual Studio. Set **Look in** to the folder you cloned or downloaded into, and search for the name of the API you're interested in. Checking **Match case** gives best results.
* Be careful of checking **Match whole word** if the API can be called in various forms&mdash;for example, **CreateMutex**, **CreateMutexA**, and **CreateMutexW**. In that case, search for **CreateMutex** with **Match whole word** unchecked.

> [!NOTE]
> You can install [Visual Studio](https://visualstudio.microsoft.com/downloads/) without expense. A Community edition is available&mdash;it's free for students, open-source contributors, and individuals. Of course you can do the same thing with any samples repo.

## The Windows classic samples repo

The main repo containing sample Windows apps using the Win32 API is the [Windows classic samples](https://github.com/Microsoft/Windows-classic-samples) repo.

## DirectX samples

See the [DirectX-Graphics-Samples](https://github.com/Microsoft/DirectX-Graphics-Samples) repo for DirectX 12 Graphics samples that demonstrate how to build graphics-intensive applications for Windows 10.

Also see [DirectX samples](/windows/uwp/gaming/directx-samples).

## Older samples

You can find some older Win32 sample apps in the [MSDN Code Gallery Microsoft samples](https://github.com/microsoftarchive/msdn-code-gallery-microsoft/tree/master/Official%20Windows%20Platform%20Sample/Windows%208.1%20desktop%20samples/%5BC%2B%2B%5D-Windows%208.1%20desktop%20samples) repo.

## See also

* [Code samples](https://developer.microsoft.com/windows/samples/)
* [Visual Studio](https://visualstudio.microsoft.com/downloads/)
* [Windows classic samples](https://github.com/Microsoft/Windows-classic-samples)
* [DirectX-Graphics-Samples](https://github.com/Microsoft/DirectX-Graphics-Samples)
* [DirectX samples](/windows/uwp/gaming/directx-samples)
* [MSDN Code Gallery Microsoft samples](https://github.com/microsoftarchive/msdn-code-gallery-microsoft)
