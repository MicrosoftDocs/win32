---
title: DirectX Frequently Asked Questions
description: This article contains a collection of Frequently Asked Questions (FAQ) about Microsoft DirectX.
ms.assetid: 58d9fe45-a2c7-8280-2826-e2e14ecea983
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DirectX Frequently Asked Questions

This article contains a collection of Frequently Asked Questions (FAQ) about Microsoft DirectX.

-   [General DirectX Development Issues](#general-directx-development-issues)
-   [Direct3D Questions](#direct3d-questions)
    -   [General Direct3D Questions](#general-direct3d-questions)
    -   [Geometry (Vertex) Processing](#geometry-vertex-processing)
    -   [Performance Tuning](#performance-tuning)
    -   [D3DX Utility Library](#d3dx-utility-library)
-   [DirectSound Questions](#directsound-questions)
-   [DirectX Extensions for Alias Maya](#directx-extensions-for-alias-maya)
-   [XInput Questions](#xinput-questions)

## General DirectX Development Issues

<dl> <dt>

<span id="Should_game_developers_really_care_about_supporting_x64_editions_"></span><span id="should_game_developers_really_care_about_supporting_x64_editions_"></span><span id="SHOULD_GAME_DEVELOPERS_REALLY_CARE_ABOUT_SUPPORTING_X64_EDITIONS_"></span>**Should game developers really care about supporting x64 editions?**
</dt> <dd>

Absolutely. x64 technology is widely available in the market. The majority of new CPUs sold in the past few years, and almost all processor lines in development from AMD and Intel, are x64-capable. Windows XP Professional x64 Edition introduced the OS enabling technology for x64 released in April of 2005. Because x64 editions require a new generation of 64-bit native drivers, this first release was limited to OEM distribution.

With Windows Vista, customers are free to choose either 32-bit or 64-bit editions when purchasing Windows-based computers, and licenses for Windows Vista are valid for both 32-bit or 64-bit editions of the OS. In addition, many 64-bit drivers are available in the box, and device manufactures are required to provide both 32-bit and 64-bit native drivers as part the Windows Certification Program.

All of these factors will greatly increase the deployments of 64-bit editions of Windows. As new computers start shipping with more than 2 GB of physical RAM, the incentive to use a 32-bit operating system greatly diminishes in favor of 64-bit editions. Sixty-four-bit technology fully supports 32-bit native code, although 64-bit native implementations are required to take full advantage of the new 64-bit memory space. Every 32-bit application should have 64-bit compatibility as a minimum shipping requirement, and meeting that requirement is a baseline requirement for Windows Vista compatibility. Incompatibilities typically arise from use of 16-bit code designed for the Windows 3.1 operating system or installing drivers that are not provided in both 32-bit and 64-bit native forms.

For more details on 64-bit technology, see [64-bit programming for Game Developers](https://msdn.microsoft.com/library/windows/desktop/ee418798).

</dd> <dt>

<span id="Should_game_developers_still_be_publishing_games_for_Windows_95__Windows_98_or_Windows_ME_"></span><span id="should_game_developers_still_be_publishing_games_for_windows_95__windows_98_or_windows_me_"></span><span id="SHOULD_GAME_DEVELOPERS_STILL_BE_PUBLISHING_GAMES_FOR_WINDOWS_95__WINDOWS_98_OR_WINDOWS_ME_"></span>**Should game developers still be publishing games for Windows 95, Windows 98 or Windows ME?**
</dt> <dd>

Not anymore for two reasons: performance and feature set.

If the minimum CPU speed required for your game is 1.2GHz or above (which is more common for high performance titles), then the vast majority of eligible computers will be running Windows XP. By the time computers with CPU speeds above 1.2GHz were being sold, Windows XP was installed as the default operating system by almost all manufacturers. This means that there are many features found in Windows XP that today's game developers should be taking advantage of including:

-   Improved multitasking - which results in a better, smoother experience for video, audio and gaming.
-   More stable video driver model - which allows easier debugging, smoother game play and better performance.
-   Easier configuration for networking - which allows easier access to multi-player games.
-   Support for DMA transfers by default from hard drives - which results in smoother, faster loading applications.
-   Windows error reporting - which results in a more stable OS, drivers and applications.
-   Unicode support - which greatly simplifies localization issues.
-   Better security and stability - which results in better consumer experiences.
-   Better support for modern hardware - most of which no longer uses Windows 98 drivers.
-   Improved memory management - which results in better stability and security.
-   Improved NTFS file system - which is more resistant to failure, and has better performance with security features.

</dd> <dt>

<span id="Should_game_developers_still_be_publishing_games_for_Windows_2000_"></span><span id="should_game_developers_still_be_publishing_games_for_windows_2000_"></span><span id="SHOULD_GAME_DEVELOPERS_STILL_BE_PUBLISHING_GAMES_FOR_WINDOWS_2000_"></span>**Should game developers still be publishing games for Windows 2000?**
</dt> <dd>

Not anymore. In addition to the reasons listed in **Should game developers still be publishing games for Windows 95, Windows 98 or Windows ME?**, Windows 2000 does not have these features:

-   Windows XP supports advanced processor features such as Hyper-Threading, Multi-Core and x64.
-   Windows XP supports side-by-side components which significantly reduces application versioning conflicts.
-   Windows XP supports no-execute memory protection which helps prevent malicious programs and can aid debugging.
-   Windows XP has improved support for advanced AGP and PCI Express based video cards.
-   Windows XP supports fast user switching, remote desktop and remote assistance which can help lower product support costs.
-   Performance tools like PIX (in the DirectX Developer SDK) no longer support Windows 2000.

In short, Windows 2000 was never designed or marketed as a consumer operating system.

</dd> <dt>

<span id="What_are_the_differences_between_the_various_editions_of_Windows_Vista__How_do_they_impact_my_DirectX_application_"></span><span id="what_are_the_differences_between_the_various_editions_of_windows_vista__how_do_they_impact_my_directx_application_"></span><span id="WHAT_ARE_THE_DIFFERENCES_BETWEEN_THE_VARIOUS_EDITIONS_OF_WINDOWS_VISTA__HOW_DO_THEY_IMPACT_MY_DIRECTX_APPLICATION_"></span>**What are the differences between the various editions of Windows Vista? How do they impact my DirectX application?**
</dt> <dd>

The Windows Vista family includes five editions:

-   Windows Vista Home Basic
-   Windows Vista Home Premium
-   Windows Vista Business
-   Windows Vista Enterprise
-   Windows Vista Ultimate

Home Basic and Home Premium are consumer-focused versions, with features like Family Safety (formerly known as Parental Controls), and Home Premium includes Media Center. Business and Enterprise are corporate-focused editions, with features like Domain join and Remote Desktop/Terminal Services. The Ultimate edition combines all features of both the consumer and corporate editions into one version. All editions come in both 32-bit (x86) and 64-bit (x64) editions, and users are free to use the same product identifier for both platforms.

The technology underlying the various editions is identical, and they all have the same version of the DirectX runtime and other components. However, the editions do have some minor differences with respect to gaming:

-   Games Explorer exists on all editions, but the Games shortcut on the Start menu is only in Home Basic, Home Premium, and Ultimate. Games Explorer can still be found on all editions (by clicking Start, pointing to All Programs, and then clicking Games), and the IGameExplorer interface functions on all editions.
-   The games that are included with Windows are not available by default on Business and Enterprise, but they can be enabled by the administrator.
-   Family Safety and game ratings do not display or have any influence on the behavior of Business or Enterprise, and they are disabled on Ultimate when a domain is joined.

User Account Control settings have the same defaults on all editions, but they can be overridden by Group Policy settings for the domain on Business, Enterprise, and Ultimate. For example, the policy setting User Account Control: Behavior of the elevation prompt for standard users may well be set to Automatically deny elevation requests in many business settings to enhance security, and many users in those environments will always be running as standard users without the ability to even choose to run as Administrator. Any program (such as an installer) that requires administrative rights, either due to legacy setup detection or to having a manifest that specifies the requested execution level as "requireAdministrator", will always fail to start in such situations. Other policy settings, such as User Account Control: Only elevate executables that are signed and validated, can also prevent your installer from functioning if you do not sign your executable file using Authenticode.

These types of policy changes can be applied to any edition of Windows Vista, but are more likely on computers that are joined to a domain.

</dd> <dt>

<span id="What_are_the_differences_between_the_various_editions_of_Windows_7__How_do_they_impact_my_DirectX_application__"></span><span id="what_are_the_differences_between_the_various_editions_of_windows_7__how_do_they_impact_my_directx_application__"></span><span id="WHAT_ARE_THE_DIFFERENCES_BETWEEN_THE_VARIOUS_EDITIONS_OF_WINDOWS_7__HOW_DO_THEY_IMPACT_MY_DIRECTX_APPLICATION__"></span>**What are the differences between the various editions of Windows 7? How do they impact my DirectX application?** 
</dt> <dd>

The majority of Windows 7 users will likely have one of two editions: Windows 7 Home Premium, for home users, or Windows 7 Professional, for business users and developers. For large corporations, there is the volume-licensed Windows 7 Enterprise edition, which includes all of Windows 7 features; Windows 7 Ultimate is the retail equivalent of that edition.

Windows 7 Starter Edition is available world-wide to OEMs, and it is expected to be deployed primarly with netbooks, ultra-low-power notebook computers. Windows 7 Home Basic is available only in emerging markets.

Note that all editions of Windows 7 (except Starter Edition) are available for both 32-bit (x86) and 64-bit (x64) versions, and all retail packages of Windows 7 include media for both versions. As with Windows Vista, users are free to use the same retail product identifier on either platform.

The underlying technology in the various editions is identical, and all editions have the same version of the DirectX runtime and other components. They do have some differences with respect to gaming features:

-   Games Explorer exists in all editions, but the Games shortcut on the Start menu is hidden by default in Windows 7 Professional and Enterprise. Games Explorer can still be found on the Start menu (by clicking All Programs and then double-clicking Games), and the direct Games shortcut can be enabled by the user.
-   The games that are included with Windows are not available by default on Windows 7 Professional and Enterprise, but they can be enabled by the administrator.
-   Family Safety and game ratings are available on all editions, but they are disabled on Windows 7 Professional, Enterprise, and Ultimate when the operating system joins a domain. As with Windows Vista Ultimate, this feature can be re-enabled on computer that has joined a domain.

User account control (UAC) settings can be affected by Group Policy settings on Windows 7 Professional, Enterprise, and Ultimate editions, much like Windows Vista. For more information, see **What are the differences between the various editions of Windows Vista? How do they impact my DirectX application?**

</dd> <dt>

<span id="Will_DirectX_10_be_available_for_Windows_XP__"></span><span id="will_directx_10_be_available_for_windows_xp__"></span><span id="WILL_DIRECTX_10_BE_AVAILABLE_FOR_WINDOWS_XP__"></span>**Will DirectX 10 be available for Windows XP?** 
</dt> <dd>

No. Windows Vista, which has DirectX 10, includes an updated DirectX runtime based on the runtime in Windows XP SP2 (DirectX 9.0c) with changes to work with the new Windows Display Driver Model (WDDM) and the new audio driver stack, and with other updates in the operating system. In addition to Direct3D 9, Windows Vista supports two new interfaces when the correct video hardware and drivers are present: Direct3D9Ex and Direct3D10.

Since these new interfaces rely on the WDDM technology, they will never be available on earlier versions of Windows. All the other changes made to DirectX technologies for Windows Vista are also specific to the new version of Windows. The name DirectX 10 is misleading in that many technologies shipping in the DirectX SDK (XACT, XINPUT, D3DX) are not encompassed by this version number. So, referring to the version number of the DirectX runtime as a whole has lost much of its meaning, even for 9.0c. The DirectX Diagnostic Tool (DXdiag.exe) on Windows Vista does report DirectX 10, but this really only refers to Direct3D 10.

</dd> <dt>

<span id="Will_DirectX_11_be_available_for_Windows_Vista_or_Windows_XP__"></span><span id="will_directx_11_be_available_for_windows_vista_or_windows_xp__"></span><span id="WILL_DIRECTX_11_BE_AVAILABLE_FOR_WINDOWS_VISTA_OR_WINDOWS_XP__"></span>**Will DirectX 11 be available for Windows Vista or Windows XP?** 
</dt> <dd>

DirectX 11 is built into Windows 7, and it is available as an update for Windows Vista (see <http://go.microsoft.com/fwlink/p/?linkid=160189>). This includes the Direct3D 11 API, DirectX Graphics Infrastructure (DXGI) 1.1, 10Level9 feature levels, Windows Advanced Rasterization Platform (WARP) 10 software rendering device, Direct2D, DirectWrite, and an update to the Direct3D 10.1 API to support 10Level9 and WARP 10.

For the same reasons noted in the preceding question (**Will DirectX 10 be available for Windows XP?** ), Direct3D 11 and related APIs are not available on Windows XP.

</dd> <dt>

<span id="What_Happened_to_DirectShow__I_can_t_find_it_in_the_DirectX_SDK._"></span><span id="what_happened_to_directshow__i_can_t_find_it_in_the_directx_sdk._"></span><span id="WHAT_HAPPENED_TO_DIRECTSHOW__I_CAN_T_FIND_IT_IN_THE_DIRECTX_SDK._"></span>**What Happened to DirectShow? I can't find it in the DirectX SDK.** 
</dt> <dd>

DirectShow was removed from the DirectX SDK as of April 2005. You can obtain the headers, libraries, tools, and samples for DirectShow in the Windows Software Development Kit (formerly known as the Platform SDK). DirectSetup in the DirectX SDK continues to support the redistribution of DirectShow's system components, and the latest components are already installed on the following operating systems: Microsoft Windows XP Service Pack 2, Windows XP Professional x64 Edition, Windows Server 2003 Service Pack 1, and Windows Vista.

</dd> <dt>

<span id="What_changes_were_made_to_the_DirectX_runtime_for_Windows_Vista__"></span><span id="what_changes_were_made_to_the_directx_runtime_for_windows_vista__"></span><span id="WHAT_CHANGES_WERE_MADE_TO_THE_DIRECTX_RUNTIME_FOR_WINDOWS_VISTA__"></span>**What changes were made to the DirectX runtime for Windows Vista?** 
</dt> <dd>

The primary changes were made to support the new WDDM. For details on the new driver model, on the impacts on Direct3D 9, and on the two new graphics interfaces, Direct3D 9Ex and Direct3D 10, please review [Graphics APIs in Windows](https://msdn.microsoft.com/library/windows/desktop/ee417756). New graphics APIs for Windows 7—Direct3D 11, Direct2D, DirectWrite, DXGI 1.1, and an updated Direct3D 10.1—are available as an update for Windows Vista (see <http://go.microsoft.com/fwlink/p/?linkid=160189>).

Windows Vista Service Pack 1 includes an updated version of the DirectX runtime. This update extends support of Windows Vista to include Direct3D 10.1, exposing new optional hardware features. (All hardware that is capable of supporting Direct3D 10.1 also fully supports all of the features of Direct3D 10.)

DirectSound was updated to expose the capabilities of the new Windows Vista audio driver stack, which supports multi-channel software buffers. The Direct3D Retained Mode API was completely removed from Windows Vista. DirectPlay Voice was also removed, as well as DirectPlay's NAT Helper and DirectInput's action-mapper UI. Support for the DirectX 7 and DirectX 8 interfaces for Visual Basic 6.0 is not available on Windows Vista.

</dd> <dt>

<span id="What_changes_were_made_to_the_DirectX_runtime_for_Windows_7__"></span><span id="what_changes_were_made_to_the_directx_runtime_for_windows_7__"></span><span id="WHAT_CHANGES_WERE_MADE_TO_THE_DIRECTX_RUNTIME_FOR_WINDOWS_7__"></span>**What changes were made to the DirectX runtime for Windows 7?** 
</dt> <dd>

Windows 7 includes all of the DirectX runtime components found in Windows Vista, and adds Direct3D 11, DXGI 1.1, 10Level9 feature levels, the WARP10 software device, Direct2D, DirectWrite, and an update to Direct3D 10.1 to support 10Level9 and WARP10. For more information, see [Graphics APIs in Windows](https://msdn.microsoft.com/library/windows/desktop/ee417756).

All other components are identical to Windows Vista, with the addition of 64-bit (x64) native support for the core DirectMusic API related to timestamped MIDI. The performance layer of DirectMusic remains deprecated, and it is only available to 32-bit applications on Windows 7 for application compatibility. Note that 64-bit native support of DirectMusic is not available on Windows Vista.

</dd> <dt>

<span id="I_think_I_have_found_a_driver_bug__what_do_I_do__"></span><span id="i_think_i_have_found_a_driver_bug__what_do_i_do__"></span><span id="I_THINK_I_HAVE_FOUND_A_DRIVER_BUG__WHAT_DO_I_DO__"></span>**I think I have found a driver bug, what do I do?** 
</dt> <dd>

First, ensure you have checked the results with the Reference Rasterizer. Then check the results with the latest WHQL certified version of the IHVs driver. You can programmatically check the WHQL status using the GetAdapterIdentifier() method on the IDirect3D9 interface passing the D3DENUM\_WHQL\_LEVEL flag.

</dd> <dt>

<span id="Why_do_I_get_so_many_error_messages_when_I_try_to_compile_the_samples__"></span><span id="why_do_i_get_so_many_error_messages_when_i_try_to_compile_the_samples__"></span><span id="WHY_DO_I_GET_SO_MANY_ERROR_MESSAGES_WHEN_I_TRY_TO_COMPILE_THE_SAMPLES__"></span>**Why do I get so many error messages when I try to compile the samples?** 
</dt> <dd>

You probably don't have your include path set correctly. Many compilers, including Microsoft Visual C++, include an earlier version of the SDK, so if your include path searches the standard compiler include directories first, you'll get incorrect versions of the header files. To remedy this issue, make sure the include path and library paths are set to search the Microsoft DirectX include and library paths first. See also the dxreadme.txt file in the SDK. If you install the DirectX SDK and you are using Visual C++, the installer can optionally set up the include paths for you.

</dd> <dt>

<span id="I_get_linker_errors_about_multiple_or_missing_symbols_for_globally_unique_identifiers__GUIDs___what_do_I_do__"></span><span id="i_get_linker_errors_about_multiple_or_missing_symbols_for_globally_unique_identifiers__guids___what_do_i_do__"></span><span id="I_GET_LINKER_ERRORS_ABOUT_MULTIPLE_OR_MISSING_SYMBOLS_FOR_GLOBALLY_UNIQUE_IDENTIFIERS__GUIDS___WHAT_DO_I_DO__"></span>**I get linker errors about multiple or missing symbols for globally unique identifiers (GUIDs), what do I do?** 
</dt> <dd>

The various GUIDs you use should be defined once and only once. The definition for the GUID will be inserted if you \#define the INITGUID symbol before including the DirectX header files. Therefore, you should make sure that this only occurs for one compilation unit. An alternative to this method is to link with the dxguid.lib library, which contains definitions for all of the DirectX GUIDs. If you use this method (which is recommended), then you should never \#define the INITGUID symbol.

</dd> <dt>

<span id="Can_I_cast_a_pointer_to_a_DirectX_interface_to_a_lower_version_number__"></span><span id="can_i_cast_a_pointer_to_a_directx_interface_to_a_lower_version_number__"></span><span id="CAN_I_CAST_A_POINTER_TO_A_DIRECTX_INTERFACE_TO_A_LOWER_VERSION_NUMBER__"></span>**Can I cast a pointer to a DirectX interface to a lower version number?** 
</dt> <dd>

No. DirectX interfaces are COM interfaces. This means that there is no requirement for higher numbered interfaces to be derived from corresponding lower numbered ones. Therefore, the only safe way to obtain a different interface to a DirectX object is to use the QueryInterface method of the interface. This method is part of the standard IUnknown interface, from which all COM interfaces must derive.

</dd> <dt>

<span id="Can_I_mix_the_use_of_DirectX_9_components_and_DirectX_8_or_earlier_components_within_the_same_application__"></span><span id="can_i_mix_the_use_of_directx_9_components_and_directx_8_or_earlier_components_within_the_same_application__"></span><span id="CAN_I_MIX_THE_USE_OF_DIRECTX_9_COMPONENTS_AND_DIRECTX_8_OR_EARLIER_COMPONENTS_WITHIN_THE_SAME_APPLICATION__"></span>**Can I mix the use of DirectX 9 components and DirectX 8 or earlier components within the same application?** 
</dt> <dd>

You can freely mix different components of differing version; for example, you could use DirectInput 8 with Direct3D 9 in the same application. However, you generally cannot mix different versions of the same component within the same application; for example, you cannot mix DirectDraw 7 with Direct3D 9 (since these are effectively the same component as DirectDraw has been subsumed into Direct3D as of DirectX 8). There are exceptions, however, such as the use of Direct3D 9 and Direct3D 10 together in the same application, which is allowed.

</dd> <dt>

<span id="Can_I_mix_the_use_of_Direct3D_9_and_Direct3D_10_within_the_same_application__"></span><span id="can_i_mix_the_use_of_direct3d_9_and_direct3d_10_within_the_same_application__"></span><span id="CAN_I_MIX_THE_USE_OF_DIRECT3D_9_AND_DIRECT3D_10_WITHIN_THE_SAME_APPLICATION__"></span>**Can I mix the use of Direct3D 9 and Direct3D 10 within the same application?** 
</dt> <dd>

Yes, you may use these versions of Direct3D together in the same application.

</dd> <dt>

<span id="What_do_the_return_values_from_the_Release_or_AddRef_methods_mean__"></span><span id="what_do_the_return_values_from_the_release_or_addref_methods_mean__"></span><span id="WHAT_DO_THE_RETURN_VALUES_FROM_THE_RELEASE_OR_ADDREF_METHODS_MEAN__"></span>**What do the return values from the Release or AddRef methods mean?** 
</dt> <dd>

The return value will be the current reference count of the object. However, the COM specification states that you should not rely on this and the value is generally only available for debugging purposes. The values you observe may be unexpected since various other system objects may be holding references to the DirectX objects you create. For this reason, you should not write code that repeatedly calls Release until the reference count is zero, as the object may then be freed even though another component may still be referencing it.

</dd> <dt>

<span id="Does_it_matter_in_which_order_I_release_DirectX_interfaces__"></span><span id="does_it_matter_in_which_order_i_release_directx_interfaces__"></span><span id="DOES_IT_MATTER_IN_WHICH_ORDER_I_RELEASE_DIRECTX_INTERFACES__"></span>**Does it matter in which order I release DirectX interfaces?** 
</dt> <dd>

It shouldn't matter because COM interfaces are reference counted. However, there are some known bugs with the release order of interfaces in some versions of DirectX. For safety, you are advised to release interfaces in reverse creation order when possible.

</dd> <dt>

<span id="What_is_a_smart_pointer_and_should_I_use_it__"></span><span id="what_is_a_smart_pointer_and_should_i_use_it__"></span><span id="WHAT_IS_A_SMART_POINTER_AND_SHOULD_I_USE_IT__"></span>**What is a smart pointer and should I use it?** 
</dt> <dd>

A smart pointer is a C++ template class designed to encapsulate pointer functionality. In particular, there are standard smart pointer classes designed to encapsulate COM interface pointers. These pointers automatically perform QueryInterface instead of a cast and they handle AddRef and Release for you. Whether you should use them is largely a matter of taste. If your code contains lots of copying of interface pointers, with multiple AddRefs and Releases, then smart pointers can probably make your code neater and less error prone. Otherwise, you can do without them. Visual C++ includes a standard Microsoft COM smart pointer, defined in the "comdef.h" header file (look up com\_ptr\_t in the help).

</dd> <dt>

<span id="I_have_trouble_debugging_my_DirectX_application__any_tips__"></span><span id="i_have_trouble_debugging_my_directx_application__any_tips__"></span><span id="I_HAVE_TROUBLE_DEBUGGING_MY_DIRECTX_APPLICATION__ANY_TIPS__"></span>**I have trouble debugging my DirectX application, any tips?** 
</dt> <dd>

The most common problem with debugging DirectX applications is attempting to debug while a DirectDraw surface is locked. This situation can cause a "Win16 Lock" on Microsoft Windows 9x systems, which prevents the debugger window from painting. Specifying the D3DLOCK\_NOSYSLOCK flag when locking the surface can usually eliminate this. Windows 2000 does not suffer from this problem. When developing an application, it is useful to be running with the debugging version of the DirectX runtime (selected when you install the SDK), which performs some parameter validation and outputs useful messages to the debugger output.

</dd> <dt>

<span id="What_s_the_correct_way_to_check_return_codes__"></span><span id="what_s_the_correct_way_to_check_return_codes__"></span><span id="WHAT_S_THE_CORRECT_WAY_TO_CHECK_RETURN_CODES__"></span>**What's the correct way to check return codes?** 
</dt> <dd>

Use the SUCCEEDED and FAILED macros. DirectX methods can return multiple success and failure codes, so a simple:

``` syntax
== D3D_OK
```

or similar test will not always suffice.

</dd> <dt>

<span id="How_do_I_disable_ALT_TAB_and_other_task_switching__"></span><span id="how_do_i_disable_alt_tab_and_other_task_switching__"></span><span id="HOW_DO_I_DISABLE_ALT_TAB_AND_OTHER_TASK_SWITCHING__"></span>**How do I disable ALT+TAB and other task switching?** 
</dt> <dd>

You don't! Games need to be able to handle task switching gracefully, as many things cause it to happen: ALT+TAB, remote desktop connections, Fast User Switching, Parental Controls usage limits, and many other events.

At the same time, two common sources of accidental task switching on games with keyboard-centric control schemes are pressing the Windows logo key and activating the accessibility feature StickyKeys with the SHIFT key. To address these cases by disabling the functionality, see the techniques described in [Disabling Shortcut Keys in Games](https://msdn.microsoft.com/library/windows/desktop/ee416808).

</dd> <dt>

<span id="Is_there_a_recommended_book_explaining_COM__"></span><span id="is_there_a_recommended_book_explaining_com__"></span><span id="IS_THERE_A_RECOMMENDED_BOOK_EXPLAINING_COM__"></span>**Is there a recommended book explaining COM?** 
</dt> <dd>

*Inside COM* by Dale Rogerson, published by Microsoft Press, is an excellent introduction to COM. For a more detailed look at COM, the book *Essential COM* by Don Box, published by Longman, is also highly recommended.

</dd> <dt>

<span id="What_is_managed_code__"></span><span id="what_is_managed_code__"></span><span id="WHAT_IS_MANAGED_CODE__"></span>**What is managed code?** 
</dt> <dd>

Managed code is code that has its execution managed by the .NET Framework Common Language Runtime (CLR). It refers to a contract of cooperation between natively executing code and the runtime. This contract specifies that at any point of execution, the runtime may stop an executing CPU and retrieve information specific to the current CPU instruction address. Information that must be query-able generally pertains to runtime state, such as register or stack memory contents.

Before the code is run, the IL is compiled into native executable code. And, since this compilation happens by the managed execution environment (or, more correctly, by a runtime-aware compiler that knows how to target the managed execution environment), the managed execution environment can make guarantees about what the code is going to do. It can insert traps and appropriate garbage collection hooks, exception handling, type safety, array bounds and index checking, and so forth. For example, such a compiler makes sure to lay out stack frames and everything just right so that the garbage collector can run in the background on a separate thread, constantly walking the active call stack, finding all the roots, chasing down all the live objects. In addition because the IL has a notion of type safety the execution engine will maintain the guarantee of type safety eliminating a whole class of programming mistakes that often lead to security holes.

In contrast this to the unmanaged world: Unmanaged executable files are basically a binary image, x86 code, loaded into memory. The program counter gets put there and that's the last the OS knows. There are protections in place around memory management and port I/O and so forth, but the system doesn't actually know what the application is doing. Therefore, it can't make any guarantees about what happens when the application runs.

</dd> <dt>

<span id="What_books_are_there_about_general_Windows_programming__"></span><span id="what_books_are_there_about_general_windows_programming__"></span><span id="WHAT_BOOKS_ARE_THERE_ABOUT_GENERAL_WINDOWS_PROGRAMMING__"></span>**What books are there about general Windows programming?** 
</dt> <dd>

Lots. However, the two that are highly recommended are:

-   Programming Windows by Charles Petzold (Microsoft Press)
-   Programming Applications for Windows by Jeffrey Richter (Microsoft Press)

</dd> <dt>

<span id="How_do_I_debug_using_the_Windows_symbol_files__"></span><span id="how_do_i_debug_using_the_windows_symbol_files__"></span><span id="HOW_DO_I_DEBUG_USING_THE_WINDOWS_SYMBOL_FILES__"></span>**How do I debug using the Windows symbol files?** 
</dt> <dd>

Microsoft publish stripped symbols for all system DLLs (plus a few others). To access them add the following to your symbol path in the project settings inside Visual Studio:

``` syntax
srv*http://msdl.microsoft.com/download/symbols
```

for caching symbols locally use the following syntax:

``` syntax
srv*c:\cache*http://msdl.microsoft.com/download/symbols
```

Where c:\\cache is a local directory for caching symbol files.

</dd> </dl>

## Direct3D Questions

### General Direct3D Questions

<dl> <dt>

<span id="Where_can_I_find_information_about_3D_graphics_techniques__"></span><span id="where_can_i_find_information_about_3d_graphics_techniques__"></span><span id="WHERE_CAN_I_FIND_INFORMATION_ABOUT_3D_GRAPHICS_TECHNIQUES__"></span>**Where can I find information about 3D graphics techniques?** 
</dt> <dd>

The standard book on the subject is Computer Graphics: Principles and Practice by Foley, Van Dam et al. It is a valuable resource for anyone wanting to understand the mathematical foundations of geometry, rasterization and lighting techniques. The FAQ for the comp.graphics.algorithms Usenet group also contains useful material.

</dd> <dt>

<span id="Does_Direct3D_emulate_functionality_not_provided_by_hardware__"></span><span id="does_direct3d_emulate_functionality_not_provided_by_hardware__"></span><span id="DOES_DIRECT3D_EMULATE_FUNCTIONALITY_NOT_PROVIDED_BY_HARDWARE__"></span>**Does Direct3D emulate functionality not provided by hardware?** 
</dt> <dd>

It depends. Direct3D has a fully featured software vertex-processing pipeline (including support for custom vertex shaders). However, no emulation is provided for pixel level operations; applications must check the appropriate caps bits and use the ValidateDevice API to determine support.

</dd> <dt>

<span id="Is_there_a_software_rasterizer_included_with_Direct3D__"></span><span id="is_there_a_software_rasterizer_included_with_direct3d__"></span><span id="IS_THERE_A_SOFTWARE_RASTERIZER_INCLUDED_WITH_DIRECT3D__"></span>**Is there a software rasterizer included with Direct3D?** 
</dt> <dd>

Not for performance applications. A reference rasterizer is supplied for driver validation but the implementation is designed for accuracy and not performance. Direct3D does support plug-in software rasterizers.

</dd> <dt>

<span id="How_can_I_perform_color_keying_with_DirectX_graphics__"></span><span id="how_can_i_perform_color_keying_with_directx_graphics__"></span><span id="HOW_CAN_I_PERFORM_COLOR_KEYING_WITH_DIRECTX_GRAPHICS__"></span>**How can I perform color keying with DirectX graphics?** 
</dt> <dd>

Color keying is not directly supported, instead you will have to use alpha blending to emulate color keying. The D3DXCreateTextureFromFileEx() function can be used to facilitate this. This function accepts a key color parameter and will replace all pixels from the source image containing the specified color with transparent black pixels in the created texture.

</dd> <dt>

<span id="Does_the_Direct3D_geometry_code_utilize_3DNow__and_or_Pentium_III_SIMD_instructions__"></span><span id="does_the_direct3d_geometry_code_utilize_3dnow__and_or_pentium_iii_simd_instructions__"></span><span id="DOES_THE_DIRECT3D_GEOMETRY_CODE_UTILIZE_3DNOW__AND_OR_PENTIUM_III_SIMD_INSTRUCTIONS__"></span>**Does the Direct3D geometry code utilize 3DNow! and/or Pentium III SIMD instructions?** 
</dt> <dd>

Yes. The Direct3D geometry pipeline has several different code paths, depending on the processor type, and it will utilize the special floating-point operations provided by the 3DNow! or Pentium III SIMD instructions where these are available. This includes processing of custom vertex shaders.

</dd> <dt>

<span id="How_do_I_prevent_transparent_pixels_being_written_to_the_z-buffer__"></span><span id="how_do_i_prevent_transparent_pixels_being_written_to_the_z-buffer__"></span><span id="HOW_DO_I_PREVENT_TRANSPARENT_PIXELS_BEING_WRITTEN_TO_THE_Z-BUFFER__"></span>**How do I prevent transparent pixels being written to the z-buffer?** 
</dt> <dd>

You can filter out pixels with an alpha value above or below a given threshold. You control this behavior by using the renderstates ALPHATESTENABLE, ALPHAREF and ALPHAFUNC.

</dd> <dt>

<span id="What_is_a_stencil_buffer__"></span><span id="what_is_a_stencil_buffer__"></span><span id="WHAT_IS_A_STENCIL_BUFFER__"></span>**What is a stencil buffer?** 
</dt> <dd>

A stencil buffer is an additional buffer of per-pixel information, much like a z-buffer. In fact, it resides in some of the bits of a z-buffer. Common stencil/z-buffer formats are 15-bit z and 1-bit stencil, or 24-bit z and 8-bit stencil. It is possible to perform simple arithmetic operations on the contents of the stencil buffer on a per-pixel basis as polygons are rendered. For example, the stencil buffer can be incremented or decremented, or the pixel can be rejected if the stencil value fails a simple comparison test. This is useful for effects that involve marking out a region of the frame buffer and then performing rendering only the marked (or unmarked) region. Good examples are volumetric effects like shadow volumes.

</dd> <dt>

<span id="How_do_I_use_a_stencil_buffer_to_render_shadow_volumes__"></span><span id="how_do_i_use_a_stencil_buffer_to_render_shadow_volumes__"></span><span id="HOW_DO_I_USE_A_STENCIL_BUFFER_TO_RENDER_SHADOW_VOLUMES__"></span>**How do I use a stencil buffer to render shadow volumes?** 
</dt> <dd>

The key to this and other volumetric stencil buffer effects, is the interaction between the stencil buffer and the z-buffer. A scene with a shadow volume is rendered in three stages. First, the scene without the shadow is rendered as usual, using the z-buffer. Next, the shadow is marked out in the stencil buffer as follows. The front faces of the shadow volume are drawn using invisible polygons, with z-testing enabled but z-writes disabled and the stencil buffer incremented at every pixel passing the z-test. The back faces of the shadow volume are rendered similarly, but decrementing the stencil value instead.

Now, consider a single pixel. Assuming the camera is not in the shadow volume there are four possibilities for the corresponding point in the scene. If the ray from the camera to the point does not intersect the shadow volume, then no shadow polygons will have been drawn there and the stencil buffer is still zero. Otherwise, if the point lies in front of the shadow volume the shadow polygons will be z-buffered out and the stencil again remains unchanged. If the points lies behind the shadow volume then the same number of front shadow faces as back faces will have been rendered and the stencil will be zero, having been incremented as many times as decremented.

The final possibility is that the point lies inside the shadow volume. In this case the back face of the shadow volume will be z-buffered out, but not the front face, so the stencil buffer will be a non-zero value. The result is portions of the frame buffer lying in shadow have non-zero stencil value. Finally, to actually render the shadow, the whole scene is washed over with an alpha-blended polygon set to only affect pixels with non-zero stencil value. An example of this technique can been seen in the "Shadow Volume" sample that comes with the DirectX SDK.

</dd> <dt>

<span id="What_are_the_texel_alignment_rules__How_do_I_get_a_one-to-one_mapping__"></span><span id="what_are_the_texel_alignment_rules__how_do_i_get_a_one-to-one_mapping__"></span><span id="WHAT_ARE_THE_TEXEL_ALIGNMENT_RULES__HOW_DO_I_GET_A_ONE-TO-ONE_MAPPING__"></span>**What are the texel alignment rules? How do I get a one-to-one mapping?** 
</dt> <dd>

This is explained fully in the Direct3D 9 documentation. However, the executive summary is that you should bias your screen coordinates by -0.5 of a pixel in order to align properly with texels. Most cards now conform properly to the texel alignment rules, however there are some older cards or drivers that do not. To handle these cases, the best advice is to contact the hardware vendor in question and request updated drivers or their suggested workaround. Note that in Direct3D 10, this rule no longer holds.

</dd> <dt>

<span id="What_is_the_purpose_of_the_D3DCREATE_PUREDEVICE_flag__"></span><span id="what_is_the_purpose_of_the_d3dcreate_puredevice_flag__"></span><span id="WHAT_IS_THE_PURPOSE_OF_THE_D3DCREATE_PUREDEVICE_FLAG__"></span>**What is the purpose of the D3DCREATE\_PUREDEVICE flag?** 
</dt> <dd>

Use the D3DCREATE\_PUREDEVICE flag during device creation to create a pure device. A pure device does not save the current state (during state changes), which often improves performance; this device also requires hardware vertex processing. A pure device is typically used when development and debugging are completed, and you want to achieve the best performance.

One drawback of a pure device is that it does not support all Get\* API calls; this means you can not use a pure device to query the pipeline state. This makes it more difficult to debug while running an application. Below is a list of all the methods that are disabled by a pure device.

-   [**IDirect3DDevice9::GetClipPlane**](https://msdn.microsoft.com/library/windows/desktop/bb174380)
-   [**IDirect3DDevice9::GetClipStatus**](https://msdn.microsoft.com/library/windows/desktop/bb174381)
-   [**IDirect3DDevice9::GetLight**](https://msdn.microsoft.com/library/windows/desktop/bb174392)
-   [**IDirect3DDevice9::GetLightEnable**](https://msdn.microsoft.com/library/windows/desktop/bb174393)
-   [**IDirect3DDevice9::GetMaterial**](https://msdn.microsoft.com/library/windows/desktop/bb174394)
-   [**IDirect3DDevice9::GetPixelShaderConstantF**](https://msdn.microsoft.com/library/windows/desktop/bb174400)
-   [**IDirect3DDevice9::GetPixelShaderConstantI**](https://msdn.microsoft.com/library/windows/desktop/bb174401)
-   [**IDirect3DDevice9::GetPixelShaderConstantB**](https://msdn.microsoft.com/library/windows/desktop/bb174399)
-   [**IDirect3DDevice9::GetRenderState**](https://msdn.microsoft.com/library/windows/desktop/bb174403)
-   [**IDirect3DDevice9::GetSamplerState**](https://msdn.microsoft.com/library/windows/desktop/bb174406)
-   [**IDirect3DDevice9::GetTextureStageState**](https://msdn.microsoft.com/library/windows/desktop/bb174413)
-   [**IDirect3DDevice9::GetTransform**](https://msdn.microsoft.com/library/windows/desktop/bb174414)
-   [**IDirect3DDevice9::GetVertexShaderConstantF**](https://msdn.microsoft.com/library/windows/desktop/bb174418)
-   [**IDirect3DDevice9::GetVertexShaderConstantI**](https://msdn.microsoft.com/library/windows/desktop/bb174419)
-   [**IDirect3DDevice9::GetVertexShaderConstantB**](https://msdn.microsoft.com/library/windows/desktop/bb174417)

A second drawback of a pure device is that it does not filter any redundant state changes. When using a pure device, your application should reduce the number of state changes in the render loop to a minimum; this may include filtering state changes to make sure that states do not get set more than once. This trade-off is application dependent; if you use more than a 1000 Set calls per frame, you should consider taking advantage of the redundancy filtering that is done automatically by a non-pure device.

As with all performance issues, the only way to know whether or not your application will perform better with a pure device is to compare your application's performance with a pure vs. non-pure device. A pure device has the potential to speed up an application by reducing the CPU overhead of the API. But be careful! For some scenarios, a pure device will slow down your application (due to the additional CPU work caused by redundant state changes). If you are not sure which type of device will work best for your application, and you do not filter redundant changes in the application, use a non-pure device.

</dd> <dt>

<span id="How_do_I_enumerate_the_display_devices_in_a_multi-monitor_system__"></span><span id="how_do_i_enumerate_the_display_devices_in_a_multi-monitor_system__"></span><span id="HOW_DO_I_ENUMERATE_THE_DISPLAY_DEVICES_IN_A_MULTI-MONITOR_SYSTEM__"></span>**How do I enumerate the display devices in a multi-monitor system?** 
</dt> <dd>

Enumeration can be performed through a simple iteration by the application using methods of the IDirect3D9 interface. Call GetAdapterCount to determine the number of display adapters in the system. Call GetAdapterMonitor to determine which physical monitor an adapter is connected to (this method returns an HMONITOR, which you can then use in the Win32 API GetMonitorInfo to determine information about the physical monitor). Determining the characteristics of a particular display adapter or creating a Direct3D device on that adapter is as simple as passing the appropriate adapter number in place of D3DADAPTER\_DEFAULT when calling GetDeviceCaps, CreateDevice, or other methods.

</dd> <dt>

<span id="What_happened_to_Fixed_Function_Bumpmapping_in_D3D9__"></span><span id="what_happened_to_fixed_function_bumpmapping_in_d3d9__"></span><span id="WHAT_HAPPENED_TO_FIXED_FUNCTION_BUMPMAPPING_IN_D3D9__"></span>**What happened to Fixed Function Bumpmapping in D3D9?** 
</dt> <dd>

As of Direct3D 9 we tightened the validation on cards that could only support > 2 simultaneous textures. Certain older cards only have 3 texture stages available when you use a specific alpha modulate operation. The most common usage that people use the 3 stages for is emboss bumpmapping, and you can still do this with D3D9.

The height field has to be stored in the alpha channel and is used to modulate the lights contribution, that is:

``` syntax
// Stage 0 is the base texture, with the height map in the alpha channel
m_pd3dDevice->SetTexture(0, m_pEmbossTexture );
m_pd3dDevice->SetTextureStageState(0, D3DTSS_TEXCOORDINDEX, 0 );
m_pd3dDevice->SetTextureStageState(0, D3DTSS_COLOROP,   D3DTOP_MODULATE );
m_pd3dDevice->SetTextureStageState(0, D3DTSS_COLORARG1, D3DTA_TEXTURE );
m_pd3dDevice->SetTextureStageState(0, D3DTSS_COLORARG2, D3DTA_DIFFUSE );
m_pd3dDevice->SetTextureStageState(0, D3DTSS_ALPHAOP,   D3DTOP_SELECTARG1 );
m_pd3dDevice->SetTextureStageState(0, D3DTSS_ALPHAARG1, D3DTA_TEXTURE );
if( m_bShowEmbossMethod )
{
 // Stage 1 passes through the RGB channels (SELECTARG2 = CURRENT), and 
 // does a signed add with the inverted alpha channel. 
 // The texture coords associated with Stage 1 are the shifted ones, so 
 // the result is:
 //    (height - shifted_height) * tex.RGB * diffuse.RGB
   m_pd3dDevice->SetTexture( 1, m_pEmbossTexture );
   m_pd3dDevice->SetTextureStageState( 1, D3DTSS_TEXCOORDINDEX, 1 );
   m_pd3dDevice->SetTextureStageState( 1, D3DTSS_COLOROP, D3DTOP_SELECTARG2 );
   m_pd3dDevice->SetTextureStageState( 1, D3DTSS_COLORARG1, D3DTA_TEXTURE );
   m_pd3dDevice->SetTextureStageState( 1, D3DTSS_COLORARG2, D3DTA_CURRENT );
   m_pd3dDevice->SetTextureStageState( 1, D3DTSS_ALPHAOP, D3DTOP_ADDSIGNED );
   m_pd3dDevice->SetTextureStageState( 1, D3DTSS_ALPHAARG1, D3DTA_TEXTURE|D3DTA_COMPLEMENT );
   m_pd3dDevice->SetTextureStageState( 1, D3DTSS_ALPHAARG2, D3DTA_CURRENT );

   // Set up the alpha blender to multiply the alpha channel 
   // (monochrome emboss) with the src color (lighted texture)
   m_pd3dDevice->SetRenderState( D3DRS_ALPHABLENDENABLE, TRUE );
   m_pd3dDevice->SetRenderState( D3DRS_SRCBLEND,  D3DBLEND_SRCALPHA );
   m_pd3dDevice->SetRenderState( D3DRS_DESTBLEND, D3DBLEND_ZERO );
}
```

This sample, along with other older samples, are no longer shipped in the current SDK release, and will not be shipped in future SDK releases.

</dd> </dl>

### Geometry (Vertex) Processing

<dl> <dt>

<span id="Vertex_streams_confuse_me_how_do_they_work__"></span><span id="vertex_streams_confuse_me_how_do_they_work__"></span><span id="VERTEX_STREAMS_CONFUSE_ME_HOW_DO_THEY_WORK__"></span>**Vertex streams confuse me how do they work?** 
</dt> <dd>

Direct3D assembles each vertex that is fed into the processing portion of the pipeline from one or more vertex streams. Having only one vertex stream corresponds to the old pre-DirectX 8 model, in which vertices come from a single source. With DirectX 8, different vertex components can come from different sources; for example, one vertex buffer could hold positions and normals, while a second held color values and texture coordinates.

</dd> <dt>

<span id="What_is_a_vertex_shader__"></span><span id="what_is_a_vertex_shader__"></span><span id="WHAT_IS_A_VERTEX_SHADER__"></span>**What is a vertex shader?** 
</dt> <dd>

A vertex shader is a procedure for processing a single vertex. It is defined using a simple assembly-like language that is assembled by the D3DX utility library into a token stream that Direct3D accepts. The vertex shader takes as input a single vertex and a set of constant values; it outputs a vertex position (in clip-space) and optionally a set of colors and texture coordinates, which are used in rasterization. Notice that when you have a custom vertex shader, the vertex components no longer have any semantics applied to them by Direct3D and vertices are simply arbitrary data that is interpreted by the vertex shader you create.

</dd> <dt>

<span id="Does_a_vertex_shader_perform_perspective_division_or_clipping__"></span><span id="does_a_vertex_shader_perform_perspective_division_or_clipping__"></span><span id="DOES_A_VERTEX_SHADER_PERFORM_PERSPECTIVE_DIVISION_OR_CLIPPING__"></span>**Does a vertex shader perform perspective division or clipping?** 
</dt> <dd>

No. The vertex shader outputs a homogenous coordinate in clip-space for the transformed vertex position. Perspective division and clipping is performed automatically post-shader.

</dd> <dt>

<span id="Can_I_generate_geometry_with_a_vertex_shader__"></span><span id="can_i_generate_geometry_with_a_vertex_shader__"></span><span id="CAN_I_GENERATE_GEOMETRY_WITH_A_VERTEX_SHADER__"></span>**Can I generate geometry with a vertex shader?** 
</dt> <dd>

A vertex shader cannot create or destroy vertices; it operates on a single vertex at a time, taking one unprocessed vertex as input and outputting a single processed vertex. It can therefore be used to manipulate existing geometry (applying deformations, or performing skinning operations) but cannot actually generate new geometry per se.

</dd> <dt>

<span id="Can_I_apply_a_custom_vertex_shader_to_the_results_of_the_fixed-function_geometry_pipeline__or_vice-versa___"></span><span id="can_i_apply_a_custom_vertex_shader_to_the_results_of_the_fixed-function_geometry_pipeline__or_vice-versa___"></span><span id="CAN_I_APPLY_A_CUSTOM_VERTEX_SHADER_TO_THE_RESULTS_OF_THE_FIXED-FUNCTION_GEOMETRY_PIPELINE__OR_VICE-VERSA___"></span>**Can I apply a custom vertex shader to the results of the fixed-function geometry pipeline (or vice-versa)?** 
</dt> <dd>

No. You have to choose one or the other. If you are using a custom vertex shader, you are responsible for performing the entire vertex transformation.

</dd> <dt>

<span id="Can_I_use_a_custom_vertex_shader_if_my_hardware_does_not_support_it__"></span><span id="can_i_use_a_custom_vertex_shader_if_my_hardware_does_not_support_it__"></span><span id="CAN_I_USE_A_CUSTOM_VERTEX_SHADER_IF_MY_HARDWARE_DOES_NOT_SUPPORT_IT__"></span>**Can I use a custom vertex shader if my hardware does not support it?** 
</dt> <dd>

Yes. The Direct3D software vertex-processing engine fully supports custom vertex shaders with a surprisingly high level of performance.

</dd> <dt>

<span id="How_do_I_determine_if_the_hardware_supports_my_custom_vertex_shader__"></span><span id="how_do_i_determine_if_the_hardware_supports_my_custom_vertex_shader__"></span><span id="HOW_DO_I_DETERMINE_IF_THE_HARDWARE_SUPPORTS_MY_CUSTOM_VERTEX_SHADER__"></span>**How do I determine if the hardware supports my custom vertex shader?** 
</dt> <dd>

Devices capable of supporting vertex shaders in hardware are required to fill out the D3DCAPS9::VertexShaderVersion field to indicate the version level of vertex shader they support. Any device claiming to support a particular level of vertex shader must support all legal vertex shaders that meet the specification for that level or below.

</dd> <dt>

<span id="How_many_constant_registers_are_available_for_vertex_shaders__"></span><span id="how_many_constant_registers_are_available_for_vertex_shaders__"></span><span id="HOW_MANY_CONSTANT_REGISTERS_ARE_AVAILABLE_FOR_VERTEX_SHADERS__"></span>**How many constant registers are available for vertex shaders?** 
</dt> <dd>

Devices supporting vs 1.0 vertex shaders are required to support a minimum of 96 constant registers. Devices may support more than this minimum number and can report this through the D3DCAPS9::MaxVertexShaderConst field.

</dd> <dt>

<span id="Can_I_share_position_data_between_vertices_with_different_texture_coordinates__"></span><span id="can_i_share_position_data_between_vertices_with_different_texture_coordinates__"></span><span id="CAN_I_SHARE_POSITION_DATA_BETWEEN_VERTICES_WITH_DIFFERENT_TEXTURE_COORDINATES__"></span>**Can I share position data between vertices with different texture coordinates?** 
</dt> <dd>

The usual example of this situation is a cube in which you want to use a different texture for each face. Unfortunately the answer is no, it's not currently possible to index the vertex components independently. Even with multiple vertex streams, all streams are indexed together.

</dd> <dt>

<span id="When_I_submit_an_indexed_list_of_primitives__does_Direct3D_process_all_of_the_vertices_in_the_buffer__or_just_the_ones_I_indexed__"></span><span id="when_i_submit_an_indexed_list_of_primitives__does_direct3d_process_all_of_the_vertices_in_the_buffer__or_just_the_ones_i_indexed__"></span><span id="WHEN_I_SUBMIT_AN_INDEXED_LIST_OF_PRIMITIVES__DOES_DIRECT3D_PROCESS_ALL_OF_THE_VERTICES_IN_THE_BUFFER__OR_JUST_THE_ONES_I_INDEXED__"></span>**When I submit an indexed list of primitives, does Direct3D process all of the vertices in the buffer, or just the ones I indexed?** 
</dt> <dd>

When using the software geometry pipeline, Direct3D first transforms all of the vertices in the range you submitted, rather than transforming them "on demand" as they are indexed. For densely packed data (that is, where most of the vertices are used) this is more efficient, particularly when SIMD instructions are available. If your data is sparsely packed (that is, many vertices are not used) then you may want to consider rearranging your data to avoid too many redundant transformations. When using the hardware geometry acceleration, vertices are typically transformed on demand as they are required.

</dd> <dt>

<span id="What_is_an_index_buffer__"></span><span id="what_is_an_index_buffer__"></span><span id="WHAT_IS_AN_INDEX_BUFFER__"></span>**What is an index buffer?** 
</dt> <dd>

An index buffer is exactly analogous to a vertex buffer, but instead it contains indices for use in DrawIndexedPrimitive calls. It is highly recommended that you use index buffers rather than raw application-allocated memory when possible, for the same reasons as vertex buffers.

</dd> <dt>

<span id="I_notice_that_32-bit_indices_are_a_supported_type__can_I_use_them_on_all_devices__"></span><span id="i_notice_that_32-bit_indices_are_a_supported_type__can_i_use_them_on_all_devices__"></span><span id="I_NOTICE_THAT_32-BIT_INDICES_ARE_A_SUPPORTED_TYPE__CAN_I_USE_THEM_ON_ALL_DEVICES__"></span>**I notice that 32-bit indices are a supported type; can I use them on all devices?** 
</dt> <dd>

No. You must check the D3DCAPS9::MaxVertexIndex field to determine the maximum index value that is supported by the device. This value must be greater than 2 to the 16th power -1 (0xffff) in order for index buffers of type D3DFMT\_INDEX32 to be supported. In addition, note that some devices may support 32-bit indices but support a maximum index value less than 2 to the 32nd power -1 (0xffffffff); in this case the application must respect the limit reported by the device.

</dd> <dt>

<span id="Does_S_W_vertex_processing_support_64_bit__"></span><span id="does_s_w_vertex_processing_support_64_bit__"></span><span id="DOES_S_W_VERTEX_PROCESSING_SUPPORT_64_BIT__"></span>**Does S/W vertex processing support 64 bit?** 
</dt> <dd>

There is an optimized s/w vertex pipeline for x64, but it does not exist for IA64.

</dd> </dl>

### Performance Tuning

<dl> <dt>

<span id="How_can_I_improve_the_performance_of_my_Direct3D_application__"></span><span id="how_can_i_improve_the_performance_of_my_direct3d_application__"></span><span id="HOW_CAN_I_IMPROVE_THE_PERFORMANCE_OF_MY_DIRECT3D_APPLICATION__"></span>**How can I improve the performance of my Direct3D application?** 
</dt> <dd>

The following are key areas to look at when optimizing performance:

<dl> <dt>

<span id="Batch_size_"></span><span id="batch_size_"></span><span id="BATCH_SIZE_"></span>**Batch size** 
</dt> <dd>

Direct3D is optimized for large batches of primitives. The more polygons that can be sent in a single call, the better. A good rule of thumb is to aim to average 1000 vertices per primitive call. Below that level you're probably not getting optimal performance, above that and you're into diminishing returns and potential conflicts with concurrency considerations (see below).

</dd> <dt>

<span id="State_changes_"></span><span id="state_changes_"></span><span id="STATE_CHANGES_"></span>**State changes** 
</dt> <dd>

Changing render state can be an expensive operation, particularly when changing texture. For this reason, it is important to minimize as much as possible the number of state changes made per frame. Also, try to minimize changes of vertex or index buffer.

> [!Note]  
> As of DirectX 8, the cost of changing vertex buffer is no longer as expensive as it was with previous versions, but it is still good practice to avoid vertex buffer changes where possible.

 

</dd> <dt>

<span id="Concurrency"></span><span id="concurrency"></span><span id="CONCURRENCY"></span>**Concurrency**
</dt> <dd>

If you can arrange to perform rendering concurrently with other processing, then you will be taking full advantage of system performance. This goal can conflict with the goal of reducing renderstate changes. You need to strike a balance between batching to reduce state changes and pushing data out to the driver early to help achieve concurrency. Using multiple vertex buffers in round-robin fashion can help with concurrency.

</dd> <dt>

<span id="Texture_uploads_"></span><span id="texture_uploads_"></span><span id="TEXTURE_UPLOADS_"></span>**Texture uploads** 
</dt> <dd>

Uploading textures to the device consumes bandwidth and causes a bandwidth competition with vertex data. Therefore, it is important to not over commit texture memory, which would force your caching scheme to upload excessive quantities of textures each frame.

</dd> <dt>

<span id="Vertex_and_index_buffers_"></span><span id="vertex_and_index_buffers_"></span><span id="VERTEX_AND_INDEX_BUFFERS_"></span>**Vertex and index buffers** 
</dt> <dd>

You should always use vertex and index buffers, rather than plain blocks of application allocated memory. At a minimum, the locking semantics for vertex and index buffers can avoid a redundant copy operation. With some drivers, the vertex or index buffer may be placed in more optimal memory (perhaps in video or AGP memory) for access by the hardware.

</dd> <dt>

<span id="State_macro_blocks_"></span><span id="state_macro_blocks_"></span><span id="STATE_MACRO_BLOCKS_"></span>**State macro blocks** 
</dt> <dd>

These were introduced in DirectX 7.0. They provide a mechanism for recording a series of state changes (including lighting, material and matrix changes) into a macro, which can then be replayed by a single call. This has two advantages:

-   You reduce the call overhead by making one call instead of many.
-   An aware driver can pre-parse and pre-compile the state changes, making it much faster to submit to the graphics hardware.

State changes can still be expensive, but using state macros can help reduce at least some of the cost. Use only a single Direct3D device. If you need to render to multiple targets, use SetRenderTarget. If you are creating a windowed application with multiple 3D windows, use the CreateAdditionalSwapChain API. The runtime is optimized for a single device and there is a considerable speed penalty for using multiple devices.

</dd> </dl> </dd> <dt>

<span id="Which_primitive_types__strips__fans__lists_and_so_on__should_I_use__"></span><span id="which_primitive_types__strips__fans__lists_and_so_on__should_i_use__"></span><span id="WHICH_PRIMITIVE_TYPES__STRIPS__FANS__LISTS_AND_SO_ON__SHOULD_I_USE__"></span>**Which primitive types (strips, fans, lists and so on) should I use?** 
</dt> <dd>

Many meshes encountered in real data feature vertices that are shared by multiple polygons. To maximize performance it is desirable to reduce the duplication in vertices transformed and sent across the bus to the rendering device. It is clear that using simple triangle lists achieves no vertex sharing, making it the least optimal method. The choice is then between using strips and fans, which imply a specific connectivity relationship between polygons and using indexed lists. Where the data naturally falls into strips and fans, these are the most appropriate choice, since they minimize the data sent to the driver. However, decomposing meshes into strips and fans often results in a large number of separate pieces, implying a large number of DrawPrimitive calls. For this reason, the most efficient method is usually to use a single DrawIndexedPrimitive call with a triangle list. An additional advantage of using an indexed list is that a benefit can be gained even when consecutive triangles only share a single vertex. In summary, if your data naturally falls into large strips or fans, use strips or fans; otherwise use indexed lists.

</dd> <dt>

<span id="How_do_you_determine_the_total_texture_memory_a_card_has__excluding_AGP_memory__"></span><span id="how_do_you_determine_the_total_texture_memory_a_card_has__excluding_agp_memory__"></span><span id="HOW_DO_YOU_DETERMINE_THE_TOTAL_TEXTURE_MEMORY_A_CARD_HAS__EXCLUDING_AGP_MEMORY__"></span>**How do you determine the total texture memory a card has, excluding AGP memory?** 
</dt> <dd>

[**IDirect3DDevice9::GetAvailableTextureMem**](https://msdn.microsoft.com/library/windows/desktop/bb174378) returns the total available memory, including AGP. Allocating resources based on an assumption of how much video memory you have is not a great idea. For example, what if the card is running under a Unified Memory Architecture (UMA) or is able to compress the textures? There might be more space available than you might have thought. You should create resources and check for 'out of memory' errors, then scale back on the textures. For example, you could remove the top mip-levels of your textures.

</dd> <dt>

<span id="What_s_a_good_usage_pattern_for_vertex_buffers_if_I_m_generating_dynamic_data__"></span><span id="what_s_a_good_usage_pattern_for_vertex_buffers_if_i_m_generating_dynamic_data__"></span><span id="WHAT_S_A_GOOD_USAGE_PATTERN_FOR_VERTEX_BUFFERS_IF_I_M_GENERATING_DYNAMIC_DATA__"></span>**What's a good usage pattern for vertex buffers if I'm generating dynamic data?** 
</dt> <dd>

1.  Create a vertex buffer using the D3DUSAGE\_DYNAMIC and D3DUSAGE\_WRITEONLY usage flags and the D3DPOOL\_DEFAULT pool flag. (Also specify D3DUSAGE\_SOFTWAREPROCESSING if you are using software vertex processing.)
2.  I = 0.
3.  Set state (textures, renderstates and so on).
4.  Check if there is space in the buffer, that is, for example, I + M <= N? (Where M is the number of new vertices).
5.  If yes, then Lock the VB with D3DLOCK\_NOOVERWRITE. This tells Direct3D and the driver that you will be adding vertices and won't be modifying the ones that you previously batched. Therefore, if a DMA operation was in progress, it isn't interrupted. If no, goto 11.
6.  Fill in the M vertices at I.
7.  Unlock.
8.  Call Draw\[Indexed\]Primitive. For non-indexed primitives use I as the StartVertex parameter. For indexed primitives, ensure the indices point to the correct portion of the vertex buffer (it may be easiest to use the BaseVertexIndex parameter of the SetIndices call to achieve this).
9.  I += M.
10. Goto 3.
11. Ok, so we are out of space, so let us start with a new VB. We don't want to use the same one because there might be a DMA operation in progress. We communicate to this to Direct3D and the driver by locking the same VB with the D3DLOCK\_DISCARD flag. What this means is "you can give me a new pointer because I am done with the old one and don't really care about the old contents any more."
12. I = 0.
13. Goto 4 (or 6).

</dd> <dt>

<span id="Why_do_I_have_to_specify_more_information_in_the_D3DVERTEXELEMENT9_structure__"></span><span id="why_do_i_have_to_specify_more_information_in_the_d3dvertexelement9_structure__"></span><span id="WHY_DO_I_HAVE_TO_SPECIFY_MORE_INFORMATION_IN_THE_D3DVERTEXELEMENT9_STRUCTURE__"></span>**Why do I have to specify more information in the D3DVERTEXELEMENT9 structure?** 
</dt> <dd>

As of Direct3D 9, the vertex stream declaration is no longer just a DWORD array, it is now an array of D3DVERTEXELEMENT9 structures. The runtime makes use of the additional semantic and usage information to bind the contents of vertex streams to vertex shaders input registers/variables. For Direct3D 9, vertex declarations are decoupled from vertex shaders, which makes it easier to use shaders with geometries of different formats as the runtime only binds the data that the shader needs.

The new vertex declarations can be used with either the fixed function pipeline or with shaders. For the fixed function pipeline, there is no need to call SetVertexShader. If however, you want to switch to the fixed function pipeline and have previously used a vertex shader, call SetVertexShader(NULL). When this is done, you will still need to call SetFVF to declare the FVF code.

When using vertex shaders, call SetVertexShader with the vertex shader object. Additionally, call SetFVF to set up a vertex declaration. This uses the information implicit in the FVF. SetVertexDeclaration can be called in place of SetFVF because it supports vertex declarations that cannot be expressed with an FVF.

</dd> </dl>

### D3DX Utility Library

<dl> <dt>

<span id="What_file_formats_are_supported_by_the_D3DX_image_file_loader_functions__"></span><span id="what_file_formats_are_supported_by_the_d3dx_image_file_loader_functions__"></span><span id="WHAT_FILE_FORMATS_ARE_SUPPORTED_BY_THE_D3DX_IMAGE_FILE_LOADER_FUNCTIONS__"></span>**What file formats are supported by the D3DX image file loader functions?** 
</dt> <dd>

The D3DX image file loader functions support BMP, TGA, JPG, DIB, PPM and DDS files.

</dd> <dt>

<span id="The_text_rendering_functions_in_D3DX_don_t_seem_to_work__what_am_I_doing_wrong__"></span><span id="the_text_rendering_functions_in_d3dx_don_t_seem_to_work__what_am_i_doing_wrong__"></span><span id="THE_TEXT_RENDERING_FUNCTIONS_IN_D3DX_DON_T_SEEM_TO_WORK__WHAT_AM_I_DOING_WRONG__"></span>**The text rendering functions in D3DX don't seem to work, what am I doing wrong?** 
</dt> <dd>

A common mistake when using the ID3DXFont::DrawText functions is to specify a zero alpha component for the color parameter; resulting in completely transparent (that is, invisible) text. For fully opaque text, ensure that the alpha component of the color parameter is fully saturated (255).

</dd> <dt>

<span id="How_can_I_save_the_contents_of_a_surface_or_texture_to_a_file__"></span><span id="how_can_i_save_the_contents_of_a_surface_or_texture_to_a_file__"></span><span id="HOW_CAN_I_SAVE_THE_CONTENTS_OF_A_SURFACE_OR_TEXTURE_TO_A_FILE__"></span>**How can I save the contents of a surface or texture to a file?** 
</dt> <dd>

The DirectX 8.1 SDK added two functions to the D3DX library specifically for this purpose: D3DXSaveSurfaceToFile() and D3DXSaveTextureToFile(). These functions support saving an image to file in either BMP or DDS format. In previous versions you will have to lock the surface and read the image data, then write it to a bitmap file. For info about writing a function to store bitmaps, see [Storing an Image](https://msdn.microsoft.com/library/windows/desktop/dd145119).

Alternatively, GDI+ could be used to save the image in a wide variety of formats, though this requires additional support files to be distributed with your application.

</dd> <dt>

<span id="How_can_I_make_use_of_the_High_Level_Shader_Language__HLSL__in_my_game__"></span><span id="how_can_i_make_use_of_the_high_level_shader_language__hlsl__in_my_game__"></span><span id="HOW_CAN_I_MAKE_USE_OF_THE_HIGH_LEVEL_SHADER_LANGUAGE__HLSL__IN_MY_GAME__"></span>**How can I make use of the High Level Shader Language (HLSL) in my game?** 
</dt> <dd>

There are three ways that the Microsoft High Level Shader Language (HLSL) can be incorporated into your game engine:

-   Compile your shader source into vertex or pixel shading assembly (using the command line utility fxc.exe) and use D3DXAssembleShader() at run time. This way even a DirectX 8 game can even take advantage of the power of the HLSL.
-   Use D3DXCompileShader() to compile your shader source into token stream and constant table form. At run time load the token stream and constant table and call CreateVertexShader() or CreatePixelShader() on the device to create your shaders.
-   The easiest way to get up and running is to take advantage of the D3DX Effects system by calling D3DXCreateEffectFromFile() or D3DXCreateEffectFromResource() with your effect file.

</dd> <dt>

<span id="What_is_the_purpose_of_the_new_shader_compiler_flag__"></span><span id="what_is_the_purpose_of_the_new_shader_compiler_flag__"></span><span id="WHAT_IS_THE_PURPOSE_OF_THE_NEW_SHADER_COMPILER_FLAG__"></span>**What is the purpose of the new shader compiler flag?** 
</dt> <dd>

Beginning with the December 2006 DirectX SDK, the new HLSL compiler that was developed for Direct3D 10 has been enabled for Direct3D 9 targets. The new compiler has no support for ps\_1\_x targets, and is now the default compiler for all Direct3D HLSL shaders. A flag for backwards compatibility can be used to force ps\_1\_x targets to compile as ps\_2\_0 targets.

Applications that do wish to use the legacy compiler can continue to do so by supplying a flag at runtime (see [**compiler flags**](https://msdn.microsoft.com/library/windows/desktop/bb205441)) or by supplying a switch when using fxc.

</dd> <dt>

<span id="What_is_the_correct_way_to_get_shaders_from_an_Effect__"></span><span id="what_is_the_correct_way_to_get_shaders_from_an_effect__"></span><span id="WHAT_IS_THE_CORRECT_WAY_TO_GET_SHADERS_FROM_AN_EFFECT__"></span>**What is the correct way to get shaders from an Effect?** 
</dt> <dd>

Use D3DXCreateEffect to create an ID3DXEffect and then use GetPassDesc to retrieve a D3DXPASS\_DESC. This structure contains pointers to vertex and pixel shaders.

Do not use ID3DXEffectCompiler::GetPassDesc. Vertex and pixel shader handles returned from this method are NULL.

</dd> <dt>

<span id="What_is_the_HLSL_noise___intrinsic_for__"></span><span id="what_is_the_hlsl_noise___intrinsic_for__"></span><span id="WHAT_IS_THE_HLSL_NOISE___INTRINSIC_FOR__"></span>**What is the HLSL noise() intrinsic for?** 
</dt> <dd>

The noise intrinsic function generates perlin noise as defined by Ken Perlin. The HLSL function can currently only be used to fill textures in texture shaders as current h/w does not support the method natively. Texture shaders are used in conjuction with the D3DXFill\*Texture() functions which are useful helper functions to generate procedurally defined textures during load time.

</dd> <dt>

<span id="How_do_I_detect_whether_to_use_pixel_shader_model_2.0_or_2.a__"></span><span id="how_do_i_detect_whether_to_use_pixel_shader_model_2.0_or_2.a__"></span><span id="HOW_DO_I_DETECT_WHETHER_TO_USE_PIXEL_SHADER_MODEL_2.0_OR_2.A__"></span>**How do I detect whether to use pixel shader model 2.0 or 2.a?** 
</dt> <dd>

You can use the D3DXGetPixelShaderProfile() and D3DXGetPixelShaderProfile() functions which return a string determining what HLSL profile is best suited to the device being ran.

</dd> <dt>

<span id="How_do_I_access_the_Parameters_in_my_Precompiled_Effects_Shaders__"></span><span id="how_do_i_access_the_parameters_in_my_precompiled_effects_shaders__"></span><span id="HOW_DO_I_ACCESS_THE_PARAMETERS_IN_MY_PRECOMPILED_EFFECTS_SHADERS__"></span>**How do I access the Parameters in my Precompiled Effects Shaders?** 
</dt> <dd>

Through the ID3DXConstantTable interface which is used to access the constant table. This table contains the variables that are used by high-level language shaders and effects.

</dd> <dt>

<span id="Is_there_a_way_to_add_user_data_to_an_effect_or_other_resource__"></span><span id="is_there_a_way_to_add_user_data_to_an_effect_or_other_resource__"></span><span id="IS_THERE_A_WAY_TO_ADD_USER_DATA_TO_AN_EFFECT_OR_OTHER_RESOURCE__"></span>**Is there a way to add user data to an effect or other resource?** 
</dt> <dd>

Yes, to set private data you call SetPrivateData (pReal is the D3D texture object, pSpoof is the wrapped texture object).

``` syntax
hr = pReal->SetPrivateData(IID_Spoof, &pSpoof, 
            sizeof(IDirect3DResource9*), 0)));
```

To look up the wrapped pointer:

``` syntax
    IDirect3DResource9* pSpoof;
    DWORD dwSize = sizeof(pSpoof);
    hr = pReal->GetPrivateData(IID_Spoof, (void*) &pSpoof, &dwSize);
```

</dd> <dt>

<span id="Why_does_rendering_of_an_ID3DXMesh_object_slow_down_significantly_after_I_define_subsets__"></span><span id="why_does_rendering_of_an_id3dxmesh_object_slow_down_significantly_after_i_define_subsets__"></span><span id="WHY_DOES_RENDERING_OF_AN_ID3DXMESH_OBJECT_SLOW_DOWN_SIGNIFICANTLY_AFTER_I_DEFINE_SUBSETS__"></span>**Why does rendering of an ID3DXMesh object slow down significantly after I define subsets?** 
</dt> <dd>

You probably have not optimized the mesh after defining the face attributes. If you specify attributes and then call ID3DXMesh::DrawSubset(), this method must perform a search of the mesh for all faces containing the requested attributes. In addition, the rendered faces are likely in a random access pattern, thus not utilizing vertex cache. After defining the face attributes for your subsets, call the ID3DXMesh::Optimize or ID3DXMesh::OptimizeInPlace methods and specifying an optimization method of D3DXMESHOPT\_ATTRSORT or stronger. Note that for optimum performance you should optimize with the D3DXMESHOPT\_VERTEXCACHE flag, which will also reorder vertices for optimum vertex cache utilization. The adjacency array generated for a D3DX Mesh has three entries per face, but some faces may not have adjacent faces on all three edges. How is this encoded? Entries where there are no adjacent faces are encoded as 0xffffffff.

</dd> <dt>

<span id="I_ve_heard_a_lot_about_Pre-computed_Radiance_Transfer__PRT___where_can_I_learn_more__"></span><span id="i_ve_heard_a_lot_about_pre-computed_radiance_transfer__prt___where_can_i_learn_more__"></span><span id="I_VE_HEARD_A_LOT_ABOUT_PRE-COMPUTED_RADIANCE_TRANSFER__PRT___WHERE_CAN_I_LEARN_MORE__"></span>**I've heard a lot about Pre-computed Radiance Transfer (PRT), where can I learn more?** 
</dt> <dd>

PRT is a new feature of D3DX added in the Summer 2003 SDK Update. It enables rendering of complex lighting scenarios such as global -llumination, soft shadowing and sub-surface scatter in real time. The SDK contains documentation and samples of how to integrate the technology into your game. The PRT Demo Sample and LocalDeformablePRT Sample samples demonstrate how to use the simulator for per vertex and per pixel lighting scenarios respectively. Further information about this and other topics can also be found at Peter Pike Sloan's Web page.

</dd> <dt>

<span id="How_can_I_render_to_a_texture_and_make_use_of_Anti_Aliasing__"></span><span id="how_can_i_render_to_a_texture_and_make_use_of_anti_aliasing__"></span><span id="HOW_CAN_I_RENDER_TO_A_TEXTURE_AND_MAKE_USE_OF_ANTI_ALIASING__"></span>**How can I render to a texture and make use of Anti Aliasing?** 
</dt> <dd>

Create a multisampled render target using Direct3DDevice9::CreateRenderTarget. After rendering the scene to that render target, StretchRect from it to a render target texture. If you make any changed to the offscreen textre (such as blurring or blooming it), copy it back to the back buffer before you present().

</dd> </dl>

## DirectSound Questions

<dl> <dt>

<span id="Why_do_I_get_a_burst_of_static_when_my_application_starts_up__I_notice_this_problem_with_other_applications_too._"></span><span id="why_do_i_get_a_burst_of_static_when_my_application_starts_up__i_notice_this_problem_with_other_applications_too._"></span><span id="WHY_DO_I_GET_A_BURST_OF_STATIC_WHEN_MY_APPLICATION_STARTS_UP__I_NOTICE_THIS_PROBLEM_WITH_OTHER_APPLICATIONS_TOO._"></span>**Why do I get a burst of static when my application starts up? I notice this problem with other applications too.** 
</dt> <dd>

You probably installed the debug DirectX runtime. The debug version of the runtime fills buffers with static in order to help developers catch bugs with uninitialized buffers. You cannot guarantee the contents of a DirectSound buffer after creation; in particular, you cannot assume that a buffer with be zeroed out.

</dd> <dt>

<span id="Why_I_am_experiencing_a_delay_in_between_changing_an_effects_parameters_and_hearing_the_results__"></span><span id="why_i_am_experiencing_a_delay_in_between_changing_an_effects_parameters_and_hearing_the_results__"></span><span id="WHY_I_AM_EXPERIENCING_A_DELAY_IN_BETWEEN_CHANGING_AN_EFFECTS_PARAMETERS_AND_HEARING_THE_RESULTS__"></span>**Why I am experiencing a delay in between changing an effects parameters and hearing the results?** 
</dt> <dd>

Changes in effect parameters do not always take place immediately on DirectX 8. For efficiency, DirectSound processes 100 milliseconds of sound data in a buffer, starting at the play cursor, before the buffer is played. This preprocessing happens after all of the following calls:

``` syntax
IDirectSoundBuffer8::SetCurrentPosition
IDirectSoundBuffer8::SetFX
IDirectSoundBuffer8::Stop
IDirectSoundBuffer8::Unlock
```

As of DirectX 9, a new FX processing algorithm that processes effects just-in-time addresses this problem and has reduced the latency. The algorithm has been added to the IDirectSoundBuffer8::Play() call, along with an additional thread that processes effects just ahead of the write cursor. So you can set parameters at any time and they'll work as expected. However, note that on a playing buffer there'll be a small delay (usually 100ms) before you hear the parameter change, because the audio between the play and write cursors (and a bit more padding) has already been processed at that time.

</dd> <dt>

<span id="How_do_I_detect_if_DSound_is_installed__"></span><span id="how_do_i_detect_if_dsound_is_installed__"></span><span id="HOW_DO_I_DETECT_IF_DSOUND_IS_INSTALLED__"></span>**How do I detect if DSound is installed?** 
</dt> <dd>

If you do not need to use DirectSoundEnumerate() to list the available DSound devices, don't link your application with dsound.lib and instead use it via COMs CoCreateInstance(CLSID\_DirectSound...) then initialize the DSound object using Initialize(NULL). If you need to use DirectSoundEnumerate(), you can dynamically load dsound.dll using LoadLibrary("dsound.dll"); and access its methods using GetProcAddress("DirectSoundEnumerateA/W") and GetProcAddress("DirectSoundCreateA/W") and so on.

</dd> <dt>

<span id="How_do_I_create_multichannel_audio_with_WAVEFORMATEXTENSIBLE__"></span><span id="how_do_i_create_multichannel_audio_with_waveformatextensible__"></span><span id="HOW_DO_I_CREATE_MULTICHANNEL_AUDIO_WITH_WAVEFORMATEXTENSIBLE__"></span>**How do I create multichannel audio with WAVEFORMATEXTENSIBLE?** 
</dt> <dd>

If you can't find an answer to your question in the DirectSound help files, there is a good article with more information available at Multiple Channel Audio Data and WAVE Files.

</dd> <dt>

<span id="How_can_I_use_the_DirectSound_Voice_Manager_with_property_sets_like_EAX__"></span><span id="how_can_i_use_the_directsound_voice_manager_with_property_sets_like_eax__"></span><span id="HOW_CAN_I_USE_THE_DIRECTSOUND_VOICE_MANAGER_WITH_PROPERTY_SETS_LIKE_EAX__"></span>**How can I use the DirectSound Voice Manager with property sets like EAX?** 
</dt> <dd>

In DirectSound 9.0 when you duplicate a buffer it is now possible to get the IDirectSoundBuffer8 interface on the duplicate buffer, which will give you access to the AcquireResources method. This will allow you to associate a buffer with the DSBCAPS\_LOCDEFER flag with a hardware resource. You can then set your EAX parameters on this buffer before having to call Play().

</dd> <dt>

<span id="I_am_having_problems_with_unreliable_behavior_when_using_cursor_position_notifications._How_can_I_get_more_accurate_information__"></span><span id="i_am_having_problems_with_unreliable_behavior_when_using_cursor_position_notifications._how_can_i_get_more_accurate_information__"></span><span id="I_AM_HAVING_PROBLEMS_WITH_UNRELIABLE_BEHAVIOR_WHEN_USING_CURSOR_POSITION_NOTIFICATIONS._HOW_CAN_I_GET_MORE_ACCURATE_INFORMATION__"></span>**I am having problems with unreliable behavior when using cursor position notifications. How can I get more accurate information?** 
</dt> <dd>

There are some subtle bugs in various versions of DirectSound, the core Windows audio stack, and audio drivers which make cursor positions notifications unreliable. Unless you're targeting a known HW/SW configuration on which you know that notifications are well-behaved, avoid cursor position notifications. For position tracking GetCurrentPosition() is a safer technique.

</dd> <dt>

<span id="I_am_suffering_from_performance_degradation_when_using_GetCurrentPosition__._What_can_I_do_to_improve_performance__"></span><span id="i_am_suffering_from_performance_degradation_when_using_getcurrentposition__._what_can_i_do_to_improve_performance__"></span><span id="I_AM_SUFFERING_FROM_PERFORMANCE_DEGRADATION_WHEN_USING_GETCURRENTPOSITION__._WHAT_CAN_I_DO_TO_IMPROVE_PERFORMANCE__"></span>**I am suffering from performance degradation when using GetCurrentPosition(). What can I do to improve performance?** 
</dt> <dd>

Each GetCurrentPosition() call on each buffer causes a system call, and system calls should be minimized as they are a large component of DSound's CPU footprint. On NT (Win2K and XP) the cursors in SW buffers (and HW buffers on some devices) move in 10ms increments, so calling GetCurrentPosition() every 10ms is ideal. Calling it more often than every 5ms will cause some performance degradation.

</dd> <dt>

<span id="My_DirectSound_application_is_taking_up_too_much_CPU_time_or_is_performing_slowly._Is_there_anything_I_can_do_to_optimize_my_code__"></span><span id="my_directsound_application_is_taking_up_too_much_cpu_time_or_is_performing_slowly._is_there_anything_i_can_do_to_optimize_my_code__"></span><span id="MY_DIRECTSOUND_APPLICATION_IS_TAKING_UP_TOO_MUCH_CPU_TIME_OR_IS_PERFORMING_SLOWLY._IS_THERE_ANYTHING_I_CAN_DO_TO_OPTIMIZE_MY_CODE__"></span>**My DirectSound application is taking up too much CPU time or is performing slowly. Is there anything I can do to optimize my code?** 
</dt> <dd>

There are several things you can do to improve the performance of your audio code:

-   Don't call GetCurrentPosition too often. Each GetCurrentPosition() call on each buffer causes a system call, and system calls should be minimized as they are a large component of DSound's CPU footprint. On NT (Win2K and XP) the cursors in SW buffers (and HW buffers on some devices) move in 10ms increments, so calling GetCurrentPosition() every 10ms is ideal. Calling it more often than every 5ms will cause some perf degradation.
-   Utilize a separate, lower frame-rate for audio. Nowadays many Windows games can exceed 100 Frames per Second and it is not necessary in most cases to update your 3D audio parameters at the same frame rate. Processing your audio every second or third graphics frame, or every 30ms or so, can reduce the number of audio calls significantly throughout your application without reducing audio quality.
-   Use DS3D\_DEFERRED for 3D objects. Most sound cards respond immediately to parameter changes and in a single frame much can change, especially if you change the position or orientation of the listener. This causes the soundcard / CPU to perform many unnecessary calculations, so another quick and universal optimization is to defer some parameter changes and commit them at the end of the frame.

    or at least use SetAllParameters rather than individual Set3DParamX calls on buffers.

    Similarly, you should use at least use SetAllParamenters calls on 3D buffers rather the individual Set3DParamX calls. Just try to minimize system calls whenever possible.

-   Don't make redundant calls; store and sort a list of play calls. Often, in one audio update frame, there are 2 requests to play new sounds. If the requests are processed as they arrive, then the first new sound could be started and then immediately replaced the second requested sound. This results in redundant calculations, an unnecessary play call, and an unnecessary stop call. It is better to store a list of requests for new sounds to be played, so that the list can be sorted, and only those voices that should start playing, are actually ever played.

    Also, you should store local copies of the 3D and EAX parameters for each sound source. If a request is made to set a parameter to a particular value, you can check to see if the value is actually different from the last value set. If it isn't, the call does not need to be made.

    Although the sound card driver will probably detect this scenario and not perform the (same) calculation again, the audio call will have to reach the audio driver (via a ring transition) and this is already a slow operation.

</dd> <dt>

<span id="When_I_stream_a_buffer_it_tends_to_glitch_and_perform_poorly._What_s_the_best_way_to_stream_a_buffer__"></span><span id="when_i_stream_a_buffer_it_tends_to_glitch_and_perform_poorly._what_s_the_best_way_to_stream_a_buffer__"></span><span id="WHEN_I_STREAM_A_BUFFER_IT_TENDS_TO_GLITCH_AND_PERFORM_POORLY._WHAT_S_THE_BEST_WAY_TO_STREAM_A_BUFFER__"></span>**When I stream a buffer it tends to glitch and perform poorly. What's the best way to stream a buffer?** 
</dt> <dd>

When streaming audio into a buffer there are two basic algorithms: After-Write-Cursor (AWC) and Before-Play-Cursor (BPC). AWC minimizes latency at the cost of glitching, whereas BPC is the opposite. Because there are usually no interactive changes to the streamed sound this sort of latency is rarely a problem for games and similar applications, so BPC is the more appropriate algorithm. In AWC, each time your streaming thread runs you "top up" the data in your looping buffers up to N ms beyond their write cursors (typically N=40 or so, to allow for Windows scheduling jitter). In BPC, you always write as much data to the buffers as possible, filling them right up to their play cursors (or perhaps 32 bytes before to allow for drivers that incorrectly report their play cursor progress).

Use BPC to mimimize glitching, and use buffers 100ms or larger even if your games doesn't glitch on your test hardware, it will glitch on some machine out there.

</dd> <dt>

<span id="I_am_playing_the_same_sounds_over_and_over_very_often_and_very_quickly_and_sometimes_they_don_t_play_properly__or_the_Play___call_takes_a_long_time._What_should_I_do__"></span><span id="i_am_playing_the_same_sounds_over_and_over_very_often_and_very_quickly_and_sometimes_they_don_t_play_properly__or_the_play___call_takes_a_long_time._what_should_i_do__"></span><span id="I_AM_PLAYING_THE_SAME_SOUNDS_OVER_AND_OVER_VERY_OFTEN_AND_VERY_QUICKLY_AND_SOMETIMES_THEY_DON_T_PLAY_PROPERLY__OR_THE_PLAY___CALL_TAKES_A_LONG_TIME._WHAT_SHOULD_I_DO__"></span>**I am playing the same sounds over and over very often and very quickly and sometimes they don't play properly, or the Play() call takes a long time. What should I do?** 
</dt> <dd>

Startup latency (which is different from streaming latency mentioned above) can be an issue in the case of some hardware (the Play() call just takes a long time sometimes on certain sound cards). If you really want to reduce this latency, for twitch sounds (gun shots, footsteps, and so on.) a handy trick is to keep some buffers always looping and playing silence. When you need to play a twitch sound, pick a free buffer, see where its write cursor is, and put the sound into the buffer just beyond the write cursor. Some soundcards fail QuerySupport for deferred properties that I know they support. Is there a workaround? You could just QuerySupport for the non-deferred versions of the properties and use deferred settings anyway. The most recent soundcard drivers may also fix this issue.

</dd> <dt>

<span id="How_do_I_encode_WAV_files_into_WMA__"></span><span id="how_do_i_encode_wav_files_into_wma__"></span><span id="HOW_DO_I_ENCODE_WAV_FILES_INTO_WMA__"></span>**How do I encode WAV files into WMA?** 
</dt> <dd>

Refer to the documentation on the Windows Media Encoder at: Windows Media Encoder 9 Series.

</dd> <dt>

<span id="How_do_I_decode_MP3_files_with_DirectSound__"></span><span id="how_do_i_decode_mp3_files_with_directsound__"></span><span id="HOW_DO_I_DECODE_MP3_FILES_WITH_DIRECTSOUND__"></span>**How do I decode MP3 files with DirectSound?** 
</dt> <dd>

DirectSound does not natively support MP3 decoding. You can decode the files in advance yourself (using an ACM codec of a DirectShow filter), or else just use DirectShow itself, which can do the decode for you; you can then copy the resulting PCM audio data into your DirectSound buffers.

</dd> </dl>

## DirectX Extensions for Alias Maya

<dl> <dt>

<span id="Why_aren_t_my_NURBS_showing_up__"></span><span id="why_aren_t_my_nurbs_showing_up__"></span><span id="WHY_AREN_T_MY_NURBS_SHOWING_UP__"></span>**Why aren't my NURBS showing up?** 
</dt> <dd>

NURBS are not supported. You can convert them to polygon meshes.

</dd> <dt>

<span id="Why_aren_t_my_SUBDs_showing_up_"></span><span id="why_aren_t_my_subds_showing_up_"></span><span id="WHY_AREN_T_MY_SUBDS_SHOWING_UP_"></span>**Why aren't my SUBDs showing up?**
</dt> <dd>

SUBDs are not supported. You can convert them to polygon meshes.

</dd> <dt>

<span id="Why_does_my_animation_in_the_X_file_look_different_than_the_animation_in_the_preview_window__"></span><span id="why_does_my_animation_in_the_x_file_look_different_than_the_animation_in_the_preview_window__"></span><span id="WHY_DOES_MY_ANIMATION_IN_THE_X_FILE_LOOK_DIFFERENT_THAN_THE_ANIMATION_IN_THE_PREVIEW_WINDOW__"></span>**Why does my animation in the X file look different than the animation in the preview window?** 
</dt> <dd>

The preview window is not animating in the strictest sense of the matter. It is not playing animation but instead is synchronizing to the most current state of Maya's scene. When animation is exported the matrices at each transform are decomposed into scale, rotation (quaternion), and translation components (often referred to as SRTs). SRTs are more desirable than matrices because they interpolate well, provide a more compact form of the data, and can be compressed independently. Not all matrices can break down into SRTs. If they cannot decompose, the resulting SRTs will be unknown, so small errors in animation may be detected. The two features in Maya that most often cause problems during decomposition are shears and off-center rotations or scales. If you are encountering this problem, because you are using off-center rotations or scales, consider adding additional transforms increasing your level of hierarchy.

Where D3DX animation supports SRTs, it looks like this:

``` syntax
[S]x[R]x[T]
```

Maya's matrices are much more complicated and require a significant amount of additional process, which looks like this:

``` syntax
[SpInv]x[S]x[Sh]x[Sp]x[St]x[RpInv]x[Ro]x[R]x[Rp]x[Rt]x[T]
```

</dd> <dt>

<span id="I_skinned_my_mesh_with_RigidSkin_but_the_mesh__or_portion__isn_t_moving._Why__"></span><span id="i_skinned_my_mesh_with_rigidskin_but_the_mesh__or_portion__isn_t_moving._why__"></span><span id="I_SKINNED_MY_MESH_WITH_RIGIDSKIN_BUT_THE_MESH__OR_PORTION__ISN_T_MOVING._WHY__"></span>**I skinned my mesh with RigidSkin but the mesh (or portion) isn't moving. Why?** 
</dt> <dd>

Maya's Rigid Skin is not supported at this time. Please use Smooth Skin.

</dd> <dt>

<span id="Where_has_all_of_my_IK_gone_in_the_X-file__"></span><span id="where_has_all_of_my_ik_gone_in_the_x-file__"></span><span id="WHERE_HAS_ALL_OF_MY_IK_GONE_IN_THE_X-FILE__"></span>**Where has all of my IK gone in the X-file?** 
</dt> <dd>

X-files do not support IK. Instead, the IK solutions are baked into the frames stored in the X-file.

</dd> <dt>

<span id="Why_do_none_of_my_materials_colors_show_up_except_DirectXShaders__"></span><span id="why_do_none_of_my_materials_colors_show_up_except_directxshaders__"></span><span id="WHY_DO_NONE_OF_MY_MATERIALS_COLORS_SHOW_UP_EXCEPT_DIRECTXSHADERS__"></span>**Why do none of my materials colors show up except DirectXShaders?** 
</dt> <dd>

The DirectX Extensions for Maya currently only support DirectXShader materials for preview and export. In a future version other materials may be supported.

</dd> </dl>

## XInput Questions

<dl> <dt>

<span id="Can_I_use_DirectInput_to_read_the_triggers__"></span><span id="can_i_use_directinput_to_read_the_triggers__"></span><span id="CAN_I_USE_DIRECTINPUT_TO_READ_THE_TRIGGERS__"></span>**Can I use DirectInput to read the triggers?** 
</dt> <dd>

Yes, but they act as the same axis. So you can not read the triggers independently with DirectInput. Using XInput, the triggers return separate values.

For more information on why DirectInput interprets the triggers as one axis, see [Using the Xbox 360 Controller with DirectInput](https://msdn.microsoft.com/library/windows/desktop/ee417014).

</dd> <dt>

<span id="How_many_controllers_does_XInput_support__"></span><span id="how_many_controllers_does_xinput_support__"></span><span id="HOW_MANY_CONTROLLERS_DOES_XINPUT_SUPPORT__"></span>**How many controllers does XInput support?** 
</dt> <dd>

XInput supports 4 controllers plugged in at a time.

</dd> <dt>

<span id="Does_XInput_support_non-common_controllers__"></span><span id="does_xinput_support_non-common_controllers__"></span><span id="DOES_XINPUT_SUPPORT_NON-COMMON_CONTROLLERS__"></span>**Does XInput support non-common controllers?** 
</dt> <dd>

No, it does not.

</dd> <dt>

<span id="Are_common_controllers_available_through_DirectInput__"></span><span id="are_common_controllers_available_through_directinput__"></span><span id="ARE_COMMON_CONTROLLERS_AVAILABLE_THROUGH_DIRECTINPUT__"></span>**Are common controllers available through DirectInput?** 
</dt> <dd>

Yes, you may access common controllers through DirectInput.

</dd> <dt>

<span id="How_do_I_get_force_feedback_on_the_common_controllers__"></span><span id="how_do_i_get_force_feedback_on_the_common_controllers__"></span><span id="HOW_DO_I_GET_FORCE_FEEDBACK_ON_THE_COMMON_CONTROLLERS__"></span>**How do I get force feedback on the common controllers?** 
</dt> <dd>

Use the [**XInputSetState**](https://msdn.microsoft.com/library/windows/desktop/ee419268) function.

</dd> <dt>

<span id="Why_does_my_default_audio_device_change__"></span><span id="why_does_my_default_audio_device_change__"></span><span id="WHY_DOES_MY_DEFAULT_AUDIO_DEVICE_CHANGE__"></span>**Why does my default audio device change?** 
</dt> <dd>

When connecting the headset, the controller's headset acts as a standard USB audio device, so when it is connected, Windows automatically changes to use this USB audio device as the default. Since the user likely does not want all audio to go through the headset, they will need to manually adjust it back to the original setting.

</dd> <dt>

<span id="How_do_I_control_the_lights_on_the_controller__"></span><span id="how_do_i_control_the_lights_on_the_controller__"></span><span id="HOW_DO_I_CONTROL_THE_LIGHTS_ON_THE_CONTROLLER__"></span>**How do I control the lights on the controller?** 
</dt> <dd>

The lights on the controller are predetermined by the operating system and can't be changed.

</dd> <dt>

<span id="How_do_I_access_the_Xbox_360_button_in_my_applications__"></span><span id="how_do_i_access_the_xbox_360_button_in_my_applications__"></span><span id="HOW_DO_I_ACCESS_THE_XBOX_360_BUTTON_IN_MY_APPLICATIONS__"></span>**How do I access the Xbox 360 button in my applications?** 
</dt> <dd>

Sorry, this button is reserved for future use.

</dd> <dt>

<span id="Where_do_I_get_drivers__"></span><span id="where_do_i_get_drivers__"></span><span id="WHERE_DO_I_GET_DRIVERS__"></span>**Where do I get drivers?** 
</dt> <dd>

The drivers will be available via Windows Update.

</dd> <dt>

<span id="How_is_controller_ID_determined__"></span><span id="how_is_controller_id_determined__"></span><span id="HOW_IS_CONTROLLER_ID_DETERMINED__"></span>**How is controller ID determined?** 
</dt> <dd>

At XInput startup, the ID is determined non-deterministically by the XInput engine and the controllers that are plugged in. If controllers are plugged in while an XInput application is running, the system will assign the new controller the lowest available number. If a controller is disconnected, its number will be made available again.

</dd> <dt>

<span id="How_do_I_get_the_audio_devices_for_the_controller__"></span><span id="how_do_i_get_the_audio_devices_for_the_controller__"></span><span id="HOW_DO_I_GET_THE_AUDIO_DEVICES_FOR_THE_CONTROLLER__"></span>**How do I get the audio devices for the controller?** 
</dt> <dd>

Use the [**XInputGetDSoundAudioDeviceGuids**](https://msdn.microsoft.com/library/windows/desktop/ee419265) function. See the AudioController sample for details.

</dd> <dt>

<span id="What_should_I_do_when_a_controller_is_unplugged__"></span><span id="what_should_i_do_when_a_controller_is_unplugged__"></span><span id="WHAT_SHOULD_I_DO_WHEN_A_CONTROLLER_IS_UNPLUGGED__"></span>**What should I do when a controller is unplugged?** 
</dt> <dd>

If the controller was in use by a player, you should pause the game until the controller is reconnected and the player presses a button to signal that they are ready to unpause.

</dd> </dl>

 

 




