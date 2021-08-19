---
title: Windows Assessment Toolkit
description: Windows Assessment Toolkit
ms.assetid: 9D0A4F42-F027-4032-8297-045937BD2B6E
ms.topic: article
ms.date: 05/31/2018
---

# Windows Assessment Toolkit

## Platforms

**Clients** - Windows 7 \| Windows 8  

## Description

The Windows Assessment Toolkit and the Windows Performance Toolkit make up the Windows Assessment and Deployment Kit (ADK). Together they provide a complete solution for evaluating overall computer performance and automating the deployment of the Windows operating system to new computers.

This topic focuses on the **Assessment Toolkit**. The assessment results are used to diagnose potential problems, so that the hardware and software that you develop are both responsive and have a minimal impact on battery life, startup performance, and shutdown time. The same assessments are available for OEM partners, ISV/IHV partners, enthusiasts, and other members of the community, to establish a common framework to measure, compare, and review aspects of quality.

By using the Windows assessment tools, you can measure different aspects of performance across a variety of scenarios, from boot time to battery-life performance to high-definition video streaming. Assessments can identify potential issues, inconsistent behavior, and highlight areas to investigate.

In previous Windows releases, multiple tools were available to measure quality, including Velocity Test Suite (VTS/VOS), Fundamental Quality Tools Suite (FQTS), and System Power and Performance Tools Suite (SPPTS). The Assessment Toolkit combines the functionality from these performance-diagnostic tools into an integrated set of tools that is easier to use and provides broader, more meaningful results.

The Windows Assessment Toolkit maximizes consumer satisfaction by:

-   Helping you to assess the overall experience of Windows, value-added software and drivers, and hardware configurations
-   Providing detailed system data that can help you identify the root causes of quality issues
-   Reducing your costs by revealing issues during development
-   Generating comparisons of results from different computers or the same set of computers over time by creating comparison graphs from multiple result sets
-   Generating feedback in a standardized format that you can use to improve the quality of your products

Important business objectives can be achieved by using the Assessments Toolkit:

-   **Measure & compare** - You can use the data to compare components (software, drivers, or both) against other similar components to facilitate your decision making, recommendations, and competitive bench marking
-   **Improve quality** - You can work independently or with involved partners to build a component (software, driver, or both) as per pre-defined quality criteria
-   **Track quality**   You can create a process for efficiently tracking quality of component versions and detect regressions after each iteration

## Usage and best practices

Assessments are a combination of XML and binary files that induce a specific set of states on a computer, measure and record the activity, and preserve the recorded results. A job is a collection of one or more assessments and their settings, run at one time on a computer. The Assessment Platform provides the infrastructure for consistently running and displaying jobs, assessments, and results. The results often include diagnostics and remediation info that helps you determine areas that need additional investigation and corrective action. You can:

-   Run assessments against a single computer or a small collection of computers with the **Windows Assessment Console** (Windows AC) <dl> This scenario is for users who want to view performance characteristics on one or several different computer configurations. Windows AC is a graphical user interface (GUI) that is used to group the assessments, create a job, package a job, run the job, and manage the job results. Results often include recommended actions.  
    </dl>
-   Run assessments against multiple computers in a lab environment with **Windows Assessment Services** (Windows AS) <dl> This scenario is primarily for users who want to run a suite of qualitative assessments against a complete line of desktops, laptops, or tablet computers in a development environment.  
    </dl>

The Assessment Toolkit offers these features:

-   A simple graphical user interface (GUI) and assessments that can be used to assess a computer without any in-depth technical knowledge of the system
-   Assessment results, viewed in the console or UI, which often include recommendations to help you improve the system
-   The ability to run a preconfigured job with one click
-   Predefined assessment settings in each preconfigured job assessment so that you can run a job on multiple computers and be confident that the results are comparable
-   Jobs that can be customized to include the assessments you want to use and the settings you want to use
-   Assessment Platform command-line syntax for scripting and automating jobs
-   The ability to run a job, view the results, take remediation steps to improve the system, and then run the job again and compare the new results side-by-side with the old results to see the how the system has improved

The Assessment Toolkit is typically used in these scenarios:




| Scenario | Description | 
|----------|-------------|
| "Black box" | Run a predefined job and examine the results for any unusual values or indications of issues with drivers, memory usage, or other areas that the assessments address. | 
| Comparing results | <ol><li>Run a single assessment using the recommended settings on any computer that is running a supported operating system.</li><li>Use the Windows AC to package the job to run on another computer.</li><li>Save the results to a share so that you can compare the results.</li><li>Compare the results from any Windows computer with those of any other supported operating system to identify differences.</li></ol><br /> | 
| Clean computer | Run assessments on a clean computer that includes only the operating system to establish baseline system results. | 
| Computer with added hardware or software components | Add new hardware or software to the clean computer system and then re-run the assessments to compare the results with clean computer results. | 
| Creating assessments | Use public APIs to develop or extend an assessment, or integrate assessments with your tools and infrastructure. | 




 

These assessments can be used:



| Assessment                                   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|----------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Driver Certification Pre-validation          | The **Driver Certification Pre-validation** assessment verifies that the drivers on a running Windows operating system qualify for the Windows Certification Program. The results include recommendations that help you resolve issues that the assessment finds, such as unsigned drivers or expired signatures.                                                                                                                                                                                                                                                            |
| Driver Verification                          | The **Driver Verification** assessment verifies that an offline Windows image or a running Windows operating system contains the correct set of drivers. The results include recommendations to help you resolve any issues that the assessment finds. These issues might include missing, duplicate, older, or unnecessary drivers.                                                                                                                                                                                                                                         |
| File Handling                                | The **File Handling** assessment provides an automated way to exercise common file operations and capture metrics. The metrics measure durations and throughput to help you understand how well a computer performs in end-user file-handling scenarios. The File Handling assessment uses a set of workloads to simulate a user who is copying, moving, compressing, uncompressing, and deleting files and folders on client systems.                                                                                                                                       |
| Photo Handling                               | The **Photo Handling** assessment measures computer performance and battery life by simulating an end user who is viewing and manipulating photos.                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Internet Explorer launch/tab create          | The **Internet Explorer Startup Performance** assessment helps identify components that can affect the time needed to start Internet Explorer. The assessment measures the time to fully render a blank page, including the load time of the IExplore.exe process and the frame-creation and tab-creation intervals. It also measures the effect of all extensions, add-ins, and toolbars that are installed on the system. It does not measure any network or browsing performance.                                                                                         |
| On/Off                                       | The **On/Off Transition** assessment measures the performance of Windows 8 boot, standby, and hibernate performance scenarios.                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Internet Explorer Browsing Performance       | The **Internet Explorer Browsing Performance** assessment measures the quality of the browsing experience in Internet Explorer, and evaluates CPU and graphic hardware capabilities. Three separate browsing workloads are provided to stress the computer in various ways.                                                                                                                                                                                                                                                                                                  |
| Media Transcoding Performance                | The **Transcode Video** assessment measures the process of changing a video file to a different format or bitrate. This assessment runs a series of transcode operations with common input and output file formats and resolutions                                                                                                                                                                                                                                                                                                                                           |
| Windows UI Performance                       | The **Windows UI Performance** assessment evaluates the performance of some basic experiences within the Windows user interface. The assessment measures responsiveness and rendering quality while the assessment exercises workloads that simulate user activities, such as using search and transitioning from Windows Store app environment to the desktop. Responsiveness results are measured in milliseconds. Low numbers mean that the computer is faster and more responsive. For rendering, the results show the frame rate and the number of glitches that occur. |
| Memory Footprint                             | You can use the **Memory Footprint** assessment to quantitatively compare a baseline operating system image against another operating system image. You can then identify the specific components that affect the memory footprint of the physical system. These components can include drivers, add-in apps, preloaded software packages, and antivirus programs.                                                                                                                                                                                                           |
| First Boot Performance                       | The **First Boot Performance** assessment identifies issues that affect how long Windows takes to boot and display the Start screen the first time the computer is started. The results help OEMs diagnose what causes delays and provide recommendations for improving the experience.                                                                                                                                                                                                                                                                                      |
| Media Streaming                              | The **Streaming Media Performance** assessment helps you assess a computer configuration's performance when you stream media using Internet Explorer. You can use the assessment results to understand, compare, and improve the streaming media experience.                                                                                                                                                                                                                                                                                                                 |
| WinSAT Comprehensive                         | The **Windows System Assessment (WinSAT)** is used to rate and improve a computer's performance in several system components, including CPU, memory, disk, and graphics. WinSAT Comprehensive assessment results express the capability of a computer s hardware configuration in numbers. Higher scores generally mean that the assessed computer performs better and faster than a computer that has a lower score.                                                                                                                                                        |
| Energy Efficiency                            | The **Energy Efficiency** job provides an automated way for you to assess the battery life of a computer. Using workloads, the Energy Efficiency job also performs diagnostics that assess whether system components are using power when they should be idle.                                                                                                                                                                                                                                                                                                               |
| MiniFilter Diagnostic Settings               | The **MiniFilter Diagnostic** option runs within the Internet Explorer Startup Performance assessment, the File Handling assessment, and the Boot Performance (Windows 8) assessment. Selecting this option within the assessments that offer the MiniFilter diagnostic option produces metrics that help you evaluate the impact of MiniFilter operations on various assessment scenarios.                                                                                                                                                                                  |
| Windows Media Player Performance and Quality | The **Windows Media Player Performance and Quality** assessment launches WMP and plays multiple media clips one after another to capture performance and quality metrics related to media playback.                                                                                                                                                                                                                                                                                                                                                                          |



 

Other tools, such as the Windows Performance Toolkit, are included in the ADK. These tools provide in-depth info enabling you to analyze and trace system and app performance. See the Resources section below for more info.

## Resources

**Video:**

-   [Channel9   BUILD ADK Videos](https://channel9.msdn.com/Events/BUILD/BUILD2011?sort=status&direction=asc&term=&t=assessment+and+deployment+kit)

  
**Documentation:**

-   [Windows Assessment and Deployment Kit](/previous-versions/windows/hh825420(v=win.10))
-   [Windows Assessment Toolkit Technical Reference](/previous-versions/windows/it-pro/windows-8.1-and-8/hh825508(v=win.10))
-   [Assessment Execution Engine](/previous-versions/windows/desktop/axe/axe-access-portal)
-   [Windows Performance Analysis](https://msdn.microsoft.com/performance/default.aspx)

  


 

