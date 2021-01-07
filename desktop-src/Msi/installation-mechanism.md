---
description: 'There are two phases to a successful installation process: acquisition and execution. If the installation is unsuccessful, a rollback phase may occur.'
ms.assetid: e9cda321-6978-4f9f-aff4-ccf609c88667
title: Installation Mechanism
ms.topic: article
ms.date: 05/31/2018
---

# Installation Mechanism

There are two phases to a successful installation process: acquisition and execution. If the installation is unsuccessful, a rollback phase may occur.

## Acquisition

At the beginning of the acquisition phase, an application or a user instructs the installer to install a feature or an application. The installer then progresses through the actions specified in the sequence tables of the installation database. These actions query the installation database and generate a script that gives a step-by-step procedure for performing the installation.

## Execution

During the execution phase, the installer passes the information to a process with elevated privileges and runs the script.

## Rollback

If an installation is unsuccessful, the installer restores the original state of the computer. When the installer processes the installation script it simultaneously generates a rollback script. In addition to the rollback script, the installer saves a copy of every file it deletes during the installation. These files are kept in a hidden, system directory. Once the installation is complete, the rollback script and the saved files are deleted. For more information, see [Rollback Installation](rollback-installation.md).

 

 



