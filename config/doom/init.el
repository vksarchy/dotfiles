;;; init.el -*- lexical-binding: t; -*-

;; This file controls what Doom modules are enabled and what order they load
;; in. Remember to run 'doom sync' after modifying it!

;; NOTE Press 'SPC h d h' (or 'C-h d h' for non-vim users) to access Doom's
;;      documentation. There you'll find a "Module Index" link where you'll find
;;      a comprehensive list of Doom's modules and what flags they support.

;; NOTE Move your cursor over a module's name (or its flags) and press 'K' (or
;;      'C-c c k' for non-vim users) to view its documentation. This works on
;;      flags as well (those symbols that start with a plus).
;;
;;      Alternatively, press 'gd' (or 'C-c c d') on a module to browse its
;;      directory (for easy access to its source code).

(doom! :input
       ;;chinese
       ;;japanese
       ;;layout            ; auie,ctsrnm is the superior home row

       :completion
       company           ; the ultimate code completion backend
       (vertico +icons)  ; a search engine for love and life (configured extensively)

       :ui
       doom              ; what makes DOOM look the way it does
       doom-dashboard    ; a nifty splash screen for Emacs (your St. Michael splash)
       hl-todo           ; highlight TODO/FIXME/NOTE/DEPRECATED/HACK/REVIEW
       ligatures         ; ligatures and symbols to make your code pretty again
       modeline          ; snazzy, Atom-inspired modeline, plus API
       ophints           ; highlight the region an operation acts on
       (popup +defaults) ; tame sudden yet inevitable temporary windows
       tabs              ; a tab bar for Emacs (centaur-tabs)
       ;;treemacs        ; a project drawer (uncomment if you use it)
       unicode           ; extended unicode support for various languages
       vc-gutter         ; vcs diff in the fringe
       vi-tilde-fringe   ; fringe tildes to mark beyond EOB
       (workspaces +layouts) ; tab emulation, persistence & separate workspaces
       zen               ; distraction-free coding or writing (writeroom-mode)

       :editor
       (evil +everywhere); come to the dark side, we have cookies
       (format +onsave)  ; automated prettiness
       snippets          ; my elves. They type so I don't have to

       :emacs
       (dired +icons)    ; making dired pretty [functional] (you use dirvish)
       electric          ; smarter, keyword-based electric-indent
       undo              ; persistent, smarter undo for your inevitable mistakes
       vc                ; version-control and Emacs, sitting in a tree

       :term
       vterm             ; the best terminal emulation in Emacs

       :checkers
       syntax            ; tasing you for every semicolon you forget
       (spell +aspell)   ; tasing you for misspelling mispelling

       :tools
       direnv            ; environment management
       editorconfig      ; let someone else argue about tabs vs spaces
       (eval +overlay)   ; run code, run (also, repls)
       lookup            ; navigate your code and its documentation
       (lsp +peek)       ; Language Server Protocol support
       tree-sitter       ; better syntax highlighting and parsing
       (magit +forge)    ; a git porcelain for Emacs
       make              ; run make tasks from Emacs
       pdf               ; pdf enhancements

       :os
       ;;(:if IS-MAC macos) ; improve compatibility with macOS
       ;;tty               ; improve the terminal Emacs experience

       :lang
       ;; Programming languages you're actively learning/using
       (python +tree-sitter +lsp)    ; beautiful is better than ugly (cybersecurity, automation)
       (rust +tree-sitter +lsp)      ; Fe2O3.unwrap() (learning)
       (emacs-lisp +tree-sitter)     ; drown in parentheses (configuring Emacs)
       
       ;; Web development (for your business sites)
       (web +tree-sitter)            ; HTML/CSS
       
       ;; Data/config formats
       (yaml +tree-sitter)           ; JSON, but readable
       
       ;; Documentation and notes
       (markdown +tree-sitter)       ; writing docs for people to ignore
       (org +pretty +roam)           ; organize your plain life in plain text
       
       ;; Shell scripting
       (sh +tree-sitter)             ; she sells {ba,z,fi}sh shells on the C xor

       :email
       ;;(mu4e)           ; Uncomment when you set up email

       :app
       calendar          ; calendar integration (you use calfw)
       (rss +org)        ; emacs as an RSS reader (elfeed)

       :config
       literate
       (default +bindings +smartparens))
