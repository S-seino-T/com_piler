#include "lex.hpp"

namespace first
{
    TokenType Lexer::get_token_type(const std::string &token)
    {
        if (token == "succ")
        {
            return TokenType::SUCC;
        }
        else if (token == "pred")
        {
            return TokenType::PRED;
        }
        else if (token == "(")
        {
            return TokenType::LPAREN;
        }
        else if (token == ")")
        {
            return TokenType::RPAREN;
        }
        else if (token == "x")
        {
            return TokenType::VAR;
        }
        else if (isdigit(token[0]))
        {
            return TokenType::NUM;
        }
        else
        {
            return TokenType::UNK;
        }
    }

    Token Lexer::get_next_token()
    {
        while (current != end && isspace(*current))
        {
            ++current;
        }
        if (current == end)
        {
            return Token(TokenType::EOT, "");
        }
        std::string token;
        while (current != end && !isspace(*current))
        {
            token += *current;
            ++current;
        }
        return Token(get_token_type(token), token);
    }

    std::vector<Token> Lexer::tokenize()
    {
        while (current != end)
        {
            tokens.push_back(get_next_token());
        }
        return tokens;
    }

    void Lexer::set_input(const std::string &input)
    {
        this->input = input;
        current = input.begin();
        end = input.end();
    }
}