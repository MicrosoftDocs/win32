---
title: Game Mode
description: The Game Mode APIs for the Universal Windows Platform (UWP) allow you to produce the most optimized gaming experience by taking advantage of Game Mode in Windows 10.
ms.assetid: a677c165-f2ba-47c6-8f6f-213a4bdefa74
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Game Mode

The Game Mode APIs for the Universal Windows Platform (UWP) allow you to produce the most optimized gaming experience by taking advantage of Game Mode in Windows 10. These APIs are located in the **&lt;expandedresources.h&gt;** header.

> [!Note]  
> These are Win32 APIs that are supported in UWP desktop and Xbox apps, as well as Win32 apps (except for [ReleaseExclusiveCpuSets](/previous-versions/windows/desktop/api/expandedresources/nf-expandedresources-releaseexclusivecpusets), which isn't supported in Win32 apps).

 

Game Mode provides customers with the best possible gaming experience by fully utilizing the capacity of their current hardware. It does this by granting a game exclusive or priority access to hardware resources. These resources being dedicated to the game help it hit performance targets more consistently. The performance increase that comes from Game Mode is directly related to the number and impact of other activities running on the device.

> [!Note]  
> The app must be in the foreground and have focus before exclusive resources are granted.

 

Game Mode works by default for most Windows games, requiring no action or opt-in by the customer, and no work by the game developer. However, you can use the Game Mode API to take it a step further and programmatically query for available system resources, determining whether the operating system considers each resource as shared or exclusive. You can leverage the available system resources in a way that best fits your game design and the configuration of the customer's system.

By using the **expandedResources** capability, you can explicitly declare that the game will work with Game Mode. As part of launching the game, the process will go into Game Mode with a set of defaults, and you can use the APIs to see what resources are available on the customer's device.

The Game Mode API has the following members:

-   [GetExpandedResourceExclusiveCpuCount](/previous-versions/windows/desktop/api/expandedresources/nf-expandedresources-getexpandedresourceexclusivecpucount): Query for details of exclusive hardware, such as cache topology, in order to rank resources.
-   [HasExpandedResources](/previous-versions/windows/desktop/api/expandedresources/nf-expandedresources-hasexpandedresources): Know when the game enters and exits Game Mode. When the game enters Game Mode, it can provide a tailored experience. When the game exits Game Mode, it can scale back the usage of resources. The general pattern is to poll once per frame.
-   [ReleaseExclusiveCpuSets](/previous-versions/windows/desktop/api/expandedresources/nf-expandedresources-releaseexclusivecpusets): Opt out of CPU exclusivity.

> [!Note]
>
> **ReleaseExclusiveCpuSets** requires the **expandedResources** restricted capability, which you can select by opening **Package.appxmanifest** in Visual Studio and navigating to the **Capabilities** tab. Alternatively, you can edit the file's code directly:
>
> <span codelanguage="XML"></span>
>
> <table>
> <colgroup>
> <col style="width: 100%" />
> </colgroup>
> <thead>
> <tr class="header">
> <th>XML</th>
> </tr>
> </thead>
> <tbody>
> <tr class="odd">
> <td><pre><code>&lt;Package
> xmlns:rescap=&quot;http://schemas.microsoft.com/appx/manifest/foundation/windows10/restrictedcapabilities&quot;
> IgnorableNamespaces=&quot; rescap&quot;&gt;
>     ...
>     &lt;Capabilities&gt;
>         &lt;rescap:Capability Name=&quot;expandedResources&quot; /&gt;
>     &lt;/Capabilities&gt;
>     ...
> &lt;/Package&gt;</code></pre></td>
> </tr>
> </tbody>
> </table>
>
> 
>
> This capability is granted on a per-title basis; contact your account manager for more information. You can publish a UWP app with this capability to the Store if it targets desktop, but if it targets Xbox it will be rejected in certification.
>
>  
>
> Games should call **HasExpandedResources** once per frame or game tick to determine whether exclusive resources have been granted. When they have been granted, the game can call [GetSystemCpuSetInformation](https://msdn.microsoft.com/library/windows/desktop/mt186425.aspx) to understand what cores the game is eligible to use. Using this function, deeper inspection, such as getting cache details, can be achieved to rank the cores for performance. The [SYSTEM\_CPU\_SET\_INFORMATION](https://msdn.microsoft.com/library/windows/desktop/mt186429.aspx) structure returned by **GetSystemCpuSetInformation** exposes details that the game can use to scale the number of threads it runs, and give threads the affinity for the appropriate cores using [SetThreadSelectedCpuSets](https://msdn.microsoft.com/library/windows/desktop/mt186428.aspx).
>
> When exclusive resources are revoked, such as when the game loses focus, the game will discover this by polling with **HasExpandedResources**, and can re-scale as appropriate. Some games may reduce the level of detail or use other tactics to maintain performance.
>
> A small number of games may choose to call **GetExpandedResourceExclusiveCpuCount** to determine what CPU resources are available for exclusive use. Based on the developer's judgment, they may opt-out of CPU exclusivity by calling **ReleaseExclusiveCpuSets** to get access to all cores, but at a higher latency due to other processes and system activities being scheduled on the same cores as the game. However, the game would still get access to other Game Mode resources, such as increased GPU prioritization. As with [SetProcessDefaultCpuSets](https://msdn.microsoft.com/library/windows/desktop/mt186427.aspx), **ReleaseExclusiveCpuSets** applies to the whole process.
>
> While CPU resources may be revoked if the game exits Game Mode, memory resources, once granted, will never be revoked. Games can use APIs such as [AppMemoryUsageLimit](https://docs.microsoft.com/uwp/api/Windows.System.MemoryManager#windows-system-memorymanager-appmemoryusagelimit) to understand what is available.
>
> ## Example: Benchmark on startup
>
> Games often do system inspection on startup to match the game experience against the system resources. Often, the methods used would involve some combination of how many CPUs are available, to scale the count of work queue threads appropriately.
>
> <span codelanguage="ManagedCPlusPlus"></span>
>
> <table>
> <colgroup>
> <col style="width: 100%" />
> </colgroup>
> <thead>
> <tr class="header">
> <th>C++</th>
> </tr>
> </thead>
> <tbody>
> <tr class="odd">
> <td><pre><code>void Game::Benchmark()
> {
>     ULONG exclusiveCpuCount;
>
>     // FastFailOnError is a user-defined function that fails fast if the given function gives an error.
>     FastFailOnError(GetExpandedResourceExclusiveCpuCount(&amp;exclusiveCpuCount));
>
>     // This sample requires 6 cores to run in Game Mode, but other games may have different requirements.
>     // Another approach may be to wait until the exclusive CPUs are given, do a cache inspection, and 
>     // then decide whether to enter Game Mode.
>     // This block works even if the app isn&#39;t currently in Game Mode.
>     if (exclusiveCpuCount &gt;= 6)
>     {
>         // m_exclusiveCapable is a user-defined boolean member variable that is true if the game can 
>         // run in Game Mode and false otherwise.
>         m_exclusiveCapable = true;
>     }
>     else
>     {
>         FastFailOnError(ReleaseExclusiveCpuSets());
>         m_exclusiveCapable = false;
>     }
>
>     // Assume shared state by default, and let the game loop update it if it&#39;s wrong. For shared mode, 
>     // the game should apply the resource set it would apply if Game Mode weren&#39;t available.
>
>     // m_hasExpandedResources is a user-defined boolean member variable that is true if the game is 
>     // running in Game Mode and false if it&#39;s running in shared mode.
>     m_hasExpandedResources = FALSE;
>
>     // m_main is a user-defined member variable that points to the main game instance. 
>     // ApplySharedModeResourceSet is a user-defined function that applies shared
>     // mode presets, possibly reducing the level of detail.
>     m_main-&gt;ApplySharedModeResourceSet();
> }</code></pre></td>
> </tr>
> </tbody>
> </table>
>
> 
>
> ## Example: Game loop
>
> **HasExpandedResources** should be called once per frame to detect state changes. This can be called in the main game loop that performs functions like collating inputs from devices and updating the world state.
>
> <span codelanguage="ManagedCPlusPlus"></span>
>
> <table>
> <colgroup>
> <col style="width: 100%" />
> </colgroup>
> <thead>
> <tr class="header">
> <th>C++</th>
> </tr>
> </thead>
> <tbody>
> <tr class="odd">
> <td><pre><code>void Game::Run()
> {
>     // m_windowClosed is a user-defined boolean member variable that is true if the app is closed and/or 
>     // in the background, and false if it&#39;s open and in the foreground.
>     while (!m_windowClosed)
>     {
>         // If the app decided that shared mode is fine, ignore game mode transitions.
>         if (m_exclusiveCapable)
>         {
>             BOOL hasExpandedResources;
>             FastFailOnError(HasExpandedResources(&amp;hasExpandedResources));
>
>             // The app has entered or exited Game Mode.
>             if (hasExpandedResources != m_hasExpandedResources)
>             {
>                 if (hasExpandedResources)
>                 {
>                     m_main-&gt;ApplySharedModeResourceSet();
>                 }
>                 else
>                 {
>                     // Games in exclusive mode can use SetProcessDefaultCpuSets and 
>                     // SetThreadSelectedCpuSets, in combination with cache information 
>                     // from GetSystemCpuSetInformation, to put busy threads on
>                     // allocated cores that have dedicated cache.
>
>                     // ApplyExclusiveModeResourcesSet is a user-defined function that 
>                     // applies Game Mode presets, perhaps increasing graphical fidelity.
>                     m_main-&gt;ApplyExclusiveModeResourcesSet();
>                 }
>
>                 m_hasExpandedResources = hasExpandedResources;
>             }
>         }
>
>         // User-defined game loop functions.
>         GameTick();
>         ProcessEvents();
>     }
> }</code></pre></td>
> </tr>
> </tbody>
> </table>
>
> 
>
> ## In this section
>
> 
>
> | Topic                                                                                           | Description                                                                                                                               |
> |-------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
> | [**GetExpandedResourceExclusiveCpuCount**](/previous-versions/windows/desktop/api/expandedresources/nf-expandedresources-getexpandedresourceexclusivecpucount)<br/> | Gets the expected number of exclusive CPU sets that are available to the app when in Game Mode.<br/>                                |
> | [**HasExpandedResources**](/previous-versions/windows/desktop/api/expandedresources/nf-expandedresources-hasexpandedresources)<br/>                                 | Gets the current resource state (that is, whether the app is running in Game Mode or shared mode).<br/>                             |
> | [**ReleaseExclusiveCpuSets**](/previous-versions/windows/desktop/api/expandedresources/nf-expandedresources-releaseexclusivecpusets)<br/>                           | Opts out of CPU exclusivity, giving the app access to all cores, but at the cost of having to share them with other processes.<br/> |
>
> 
>
>  
>
>  
>
>  
>




