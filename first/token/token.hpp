#pragma once
#include "../common/pch.hpp"

namespace first
{

    enum class TokenType
    {
        NUM,
        VAR,
        SUCC,
        PRED,
        LPAREN,
        RPAREN,
        UNK, // Unknown
        EOT, // End of Token
    };

    class Token
    {
    public:
        TokenType type;
        std::string value;
        Token(TokenType type, const std::string &value) : type(type), value(value) {}
        ~Token() = default;
        friend std::ostream &operator<<(std::ostream &os, const Token &token);
        std::string to_string() const;
    };

    std::string type_to_string(TokenType type);
    std::ostream &operator<<(std::ostream &os, const Token &token);
    // std::string Token::to_string() const;
}