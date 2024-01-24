---
description: There are essentially no constraints on how to write an AutoRun startup application.
ms.assetid: 6D95E5F0-8D93-47A8-9D8C-49CBDCA150A7
title: How to Implement AutoRun Startup Applications
ms.topic: article
ms.date: 05/31/2018
---

# How to Implement AutoRun Startup Applications

There are essentially no constraints on how to write an AutoRun startup application. You can implement the startup application to do whatever you find necessary to install, uninstall, configure, or run your application. However, the following tips provide some guidelines to implementing an effective AutoRun startup application.

## Instructions

### Step 1:

Make sure that users receive feedback as soon as possible after they insert an AutoRun disc into the drive. Startup applications should be small programs that load quickly. They should clearly identify the application and provide an easy way to cancel the operation.

### Step 2:

Check to see if the program is already installed. If not, the next step will probably be the setup procedure. The startup application can take advantage of the time the user spends reading the dialog box by starting another thread to begin loading the setup code. By the time the user clicks **OK**, your setup program will already be partly if not fully loaded. This approach significantly reduces the user's perception of the amount of time it takes to load your application.

> [!Note]  
> Typically, the initial part of the startup application presents users with a user interface, such as a dialog box, asking them how they would like to proceed.

 

### Step 3:

Start another thread to begin loading application code to shorten the waiting time for the user. If the application has already been installed, the user probably inserted the disk to run the application.

### Step 4:

Use the following hints to minimize hard disk usage:

-   Keep the number of files that must be on the hard disk to a minimum. They should be restricted to files that are essential to running the program or that would take an unacceptably large amount of time to read from the media.
-   In many cases, installing nonessential files on the hard disk is not necessary, but might provide benefits such as increased performance. Give the user the option of deciding how to make the trade-off between the costs and benefits of hard disk storage.
-   Provide a way to uninstall any components that were placed on the hard disk.
-   If your application caches data, give the user some control over it. Include options in the startup application such as setting a limit on the maximum amount of cached data that will be stored on the hard disk, or having the application discard any cached data when it terminates.

### Step 5:

Disable Autorun if needed. AutoRun can be suppressed programmatically or disabled entirely with the registry, even when a medium has an Autorun.inf file. See [Enabling and Disabling AutoRun](autoplay-reg.md) for more information.

 

 



