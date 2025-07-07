#pragma once
#include "../common/pch.hpp"
#include "../token/token.hpp"

namespace first
{
    class Lexer
    {
    public:
        Lexer(const std::string &input) : input(input), current(input.begin()), end(input.end()) {}
        ~Lexer() = default;
        void set_input(const std::string &input);
        std::vector<Token> tokenize();

    private:
        std::string input;
        std::string::const_iterator current;
        std::string::const_iterator end;
        std::vector<Token> tokens;
        Token get_next_token();
        TokenType get_token_type(const std::string &token);
    };
}