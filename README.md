# LabSpecDB

## A git repository for cataloging laboratory spectroscopy data

There are two folders: `catalog` and `input`. Please put the right file in the right place!

---

## Usage:

### Setup

Clone this repository to your computer with:

`git clone https://github.com/laserkelvin/LabSpecDB.git`

This will clone the `master` branch, which should be the most stable version of the database.

### Updating your local database from remote Git

This will update your local database with the newest on Git.

`git fetch`

`git pull`

### Creating a new branch

Running `git checkout -b [name of branch]` will create a new branch locally. If you want to push this onto the web, you'll have to add a remote branch:

`git push --set-upstream origin [name of branch]`

### Updating the remote database

See https://git-scm.com/docs/git-request-pull

When you want to contribute new files, it may be best to have your own personal branch. Routine

Preferably, you will have your own analysis scripts to point to the folder, and adjust your usage accordingly. The plan is to also include scripts (to be written) that will generate the catalog files systematically, and perhaps some rudimentary searching functionality.

A sample `template.int` is provided in input, where you should only add/remove dipole moments, as well as the partition function at 300 K.

---

## Formatting of the files

Catalog files can have two file extensions: `.list` or `.cat`

### List files

These are either a list of frequencies, or `x,y` column format with frequency
and intensity.

### Catalog files

1. In the format of SPCAT
2. Intensities calculated at 300 K
3. If available, the `.par`, `.var`, `.lin`, and `.int` files in the folder
`input`
4. Calculate frequencies up to 1000 GHz
5. When possible, catalog files include measured frequencies (`calmrg`)

---

##Naming convention

1. Capital letter atoms
2. Separated by underscores
3. Vibrational states are referenced by digits, with the index corresponding
to the normal modes ordered by __frequency__:
    - For a triatomic:
        - _000_ is the ground state,
        - _010_ is $\nu_2=1$ (_NOT_ the bend!)
4. Isotopologues
    - Mass + Atom
    - e.g. _13C_

Example for $\mathrm{C_3S}$ vibrational ground state, normal species:

C3S_00000.cat

Example for $\mathrm{C_3S}$ with one $^{13}$C, $\nu_4=2$:

C3S_C13_00020.list

For $l \neq 0$ states:

C3S_C13-1_00002-l1.cat

For cyclic molecules:

C3H2-c_xxx.cat

For electronically excited states, put the state label at the end. For example,
the $A$ state of SO with v=2:

SO_2_A.cat

When in doubt, use the typical naming order, which orders carbon first, then
hydrogen, then oxygen and so on.
