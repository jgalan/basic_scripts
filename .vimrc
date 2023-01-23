set foldmethod=syntax

syntax on

nnoremap <F5> :buffers<CR>:buffer<Space>
nnoremap <F6> :b#<CR>


filetype plugin indent on
" show existing tab with 4 spaces width
set tabstop=4
" when indenting with '>', use 4 spaces width
set shiftwidth=4
" On pressing tab, insert 4 spaces
"set expandtab
set tags=$HOME/git/tags

":set noet ci pi sts=0 sw=4 ts=4
"
" Only when editing tex files I am interested on syntax folding
"autocmd FileType tex 
"set foldmethod=manual
"set number
"
let g:clang_format#style_options = {
             \ "AccessModifierOffset" : -4,
             \ "ColumnLimit" : 60,
             \ "AllowShortIfStatementsOnASingleLine" : "true",
             \ "AlwaysBreakTemplateDeclarations" : "false",
             \ "Standard" : "C++11"}
 
let g:fold_options = {
    \ 'fallback_method' : { 'line_threshold' : 2000, 'method' : 'syntax' },
    \ 'fold_blank': 0,
    \ 'fold_includes': 0,
    \ 'max_foldline_length': 'win',
    \ 'merge_comments' : 1,
    \ 'show_if_and_else': 1,
   \ 'strip_namespaces': 1,
    \ 'strip_template_arguments': 1
    \ }

map <C-K> :ClangFormat<cr>
imap <C-K> <c-o>:ClangFormat<cr>
autocmd FileType c,cpp ClangFormatAutoEnable

autocmd BufNewFile,BufRead *.rms set syntax=xml
