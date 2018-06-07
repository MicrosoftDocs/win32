---
Description: 'When you want to create a new desktop app, the first decision you make is whether to use the Win32 and COM API or .NET.'
ms.assetid: '82705644-F1F0-40F3-99B1-7A97BFB32831'
title: Choose Your Technology
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Choose Your Technology

When you want to create a new desktop app, the first decision you make is whether to use the Win32 and COM API or .NET. Both options let you create desktop apps like Word, Excel, and Photoshop that run in the classic Windows desktop and take full advantage of that environment's specific features.

 

Here are a few of the major differences between Wind32 and .NET technologies and when they are appropriate to use:



|                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |                |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------|
| **NET/XAML:**      | Languages: C\#, C++, F\#, VB<br/> Best if you need to have a higher level of coding and productivity, or to use a less complex language for which it might be easier to hire talent. <br/> You can also share some .NET Framework code and libraries between Windows Store, Windows Phone, Windows desktop applications, and other Microsoft platforms by using portable class libraries.<br/>                                                                                                                                                                                                                                                   |    <br/> |
| **C++ and Win32:** | Languages: C++ with COM<br/> Best if you need to achieve the highest levels of performance or efficiency, access native OS features, or want to target DirectX technologies. <br/> C++ and Win32 gets you "closer to the metal," and lets you achieve the best performance for your app by taking direct control over memory allocation and performance-oriented CPU features like SSE or AVX instructions. It is the best way to target DirectX technologies for low-level, high-performance graphics access.<br/> You can share C++ code between Windows, Windows Phone, and Windows Store, as well as with non-Windows platforms. <br/> |    <br/> |



 

## Choose .NET

.NET provides a consistent, first-class development experience across the desktop, Windows Phone, and Windows Store. It offers a higher level of coding and productivity. .NET allows you to keep developing foundational apps on the desktop and add exciting new experiences, all while using your existing skills and reusing code between devices. If you are looking to create more tailored, platform-appropriate experiences on any device, Visual Studio Industry Partners (VSIP) provide solutions that enable re-using C\# skills and code with non-Windows devices.

In addition to features you expect such as files/streams and network communication, here are a few highlights of what .NET offers to make building applications very productive:

-   Runtime productivity and safety such as automatic memory management, type safety, exception handling, and thread management
-   GUI technologies   see below
-   Rich collection data types
-   Data modeling (ADO, LINQ, WCF data services)
-   Language Integrated Query (LINQ)
-   Date and time library
-   Serialization
-   Web services
-   Security and cryptography
-   Parallel programming library

**Choose a UI stack:** Desktop applications can choose between two UI stacks. Data-centric applications benefit from data binding features in both for displaying data. The following provides guidance on choosing between the two UI stacks:

-   **.NET Windows Presentation Foundation (WPF):** This is the preferred technology for Windows-based desktop applications that require UI complexity, styles customization, and graphics-intensive scenarios for the desktop. WPF also takes advantage of XAML views. You can leverage the new simplified asynchronous capabilities (async/await) in .NET 4.5. WPF development skills are similar to Windows Store development skills, so migration from WPF to Windows Store apps is easier than migration from Windows Forms.
-   **.NET Windows Forms:** .This was the first UI technology in the .NET Framework for building desktop applications. It is still a good fit for many business desktop applications. Windows Forms is easier to use and lighter weight than WPF for simple scenarios. Windows Forms does not use XAML, so deciding later to extend your application to Windows Phone or Windows Store entails a complete re-write of your UI.

**Other capabilities** .NET provides multiple innovations to you to extend your app to new platforms without changes in the architecture. You can often re-use code, and the following .NET features make that easier:

-   **Model-View-ViewModel design pattern (MVVM):** Microsoft client platforms (including WPF) make it easy to build applications using the MVVM pattern. With this pattern you get a strong separation of display from application state, logic, and behaviors, which will help you to create clean and maintainable code that can be easily shared between multiple devices.
-   **Portable class libraries:** .NET portable libraries allow binaries to be shared between multiple platforms such as the desktop, Windows Store, Windows Phone, and other applications. Implementing your client logic with .NET portable libraries will greatly simplify the creation of multiple experiences on multiple platforms.
-   **Modernize your user experience:** Concepts that are demanded by today s users can be implemented with the latest innovations on .NET for the desktop. Design principles such as  fast and fluid,   authentically digital,  or  do more with less  can be applied to your existing desktop application by employing a modern UI for your XAML design, carefully using animations, and implementing .NET asynchronous programming extensively.

For further reading and more depth, there is a description of .NET technologies and guidance for various applications in [.NET Technology Guide for Business Applications](http://download.microsoft.com/download/1/6/E/16E9FC39-0D61-4DB8-AADE-9F6950B8BF49/Microsoft_Press_eBook_NET_Technology_Guide_for_Business_Applications.pdf) for which there is a summary.

## Choosing C++ and Win32

C++ provides a first-class development experience across a wide range of platforms, both Windows and non-Windows, without depending on a high-level runtime environment like .NET. This makes C++ the language of choice for portable applications when such runtimes are unavailable or too heavyweight for certain target platforms.

Using C++ and the Win32 API makes it possible to achieve the highest levels of performance and efficiency by taking tighter control of the target platform than the .NET runtime allows. However, exercising such a level of control over your application's execution requires greater care and attention to get right, and trades development productivity for runtime performance.

Here are a few highlights of what C++ offers to enable you to build high-performance applications.

-   Hardware-level optimizations, including tight control over resource allocation, object lifetimes, data layout, alignment, byte packing, and more.
-   Access to performance-oriented instruction sets like SSE and AVX through intrinsic functions.
-   Efficient, type-safe generic programming by using templates.
-   Efficient and safe containers and algorithms.
-   DirectX in particular Direct3D and DirectCompute.
-   C++ AMP

### C++ for games and graphics-rich applications

If there's one domain where C++ is the clear winner, games is it -- or apps that demand similar levels of graphics and processing performance. C++ is ideally suited to these kinds of apps because it enables the programmer to manage resources and object lifetimes explicitly; it provides access to hardware-level optimization opportunities; it can access DirectX and other performance-oriented Win32 libraries more directly than a managed language; and it makes available a number of quality game development libraries.

Even while there are great technologies available for making games that are less performance intensive in managed languages like C\#, the managed environment makes it difficult or impossible to match the level of performance that can be achieved by C++ developers. When absolute performance is the goal or when any overhead is too much--as when bringing big experiences to small devices--C++ is the go-to language.

### C++ for traditional desktop applications

Writing a traditional, UI-heavy desktop application like a spreadsheet, word processor, or line-of-business application in C++ makes the most sense when the application is computationally intensive, or when there is a substantial amount of existing C++ code that you can use to build it. Otherwise, managed languages have adequate performance and the .NET ecosystem offers increased productivity due to its more-modern application and UI frameworks, and its more-capable standard library.

When writing a desktop application in C++, you can choose MFC or Win32 for the UI, or a host of third-party application frameworks that also support non-Windows platforms.

-   **MFC (Microsoft Foundation Class Library):** This is the venerable application framework and UI library that has served Windows developers since 1992. It's a thin C++ wrapper over the handle-based, C-language Win32 API and provides object-oriented interfaces for many of the predefined windows, common controls, and other Windows objects. Although many modern UI frameworks in the .NET ecosystem surpass MFC in convenience, it is still the native UI framework of choice for many C++ developers creating applications for the Windows desktop.
-   **Win32:** This is the handle-based, C-language API of the Windows platform, including but not limited to UI functionality such as windowing, drawing, and UI controls. Because it is a low-level, C-language API based on handles, it's an infrequent choice for creating modern, UI-intensive apps. However, it supplies the basic APIs necessary to interact with the Windows platform, and is a suitable choice for apps that have simple UI requirements or that just want the Windows UI to stay out of the way as much as possible for example, games.
-   **Third-party application frameworks:** Because C++ can run on a wide variety of platforms and isn't tied to Windows or the .NET runtime, third-parties have developed new application and UI frameworks for C++ to ease development of cross-platform applications with rich user interfaces. Some of these frameworks provide their own look & feel, while others such as wxWidgets or Qt use or emulate the native control set of the platform. Using these libraries, it's possible to share nearly all of an application's source code between versions of the application that run on Windows or other platforms, such as OSX or Linux.

## Conclusion

You may have a strong affinity to C++ or C\#/Visual Basic, and that may determine how you choose to write desktop applications. Use .NET/C\# (or Visual Basic) for high level coding, more productivity, rich frameworks and services, support for modern customer experiences, and cross platform maintenance of assets (Windows Store apps, Windows Phone apps, Windows desktop apps, and others). Use native C++ for games and other graphics-intensive applications, when you need to achieve the highest levels of performance, to manage resources or memory layout explicitly, to access hardware-level optimization opportunities, when you want your application to be portable to platforms without the .NET runtime, or to more readily take advantage of freely available, high-quality C and C++ libraries that exists.

 

 




