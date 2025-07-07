#include "token.hpp"

namespace first
{

    std::string Token::to_string() const
    {
        return "Token(" + type_to_string(type) + ", '" + value + "')";
    }

    std::string type_to_string(TokenType type)
    {
        // ... switch文そのまま ...
        switch (type)
        {
        case TokenType::NUM:
            return "NUM";
        case TokenType::VAR:
            return "VAR";
        case TokenType::SUCC:
            return "SUCC";
        case TokenType::PRED:
            return "PRED";
        case TokenType::LPAREN:
            return "LPAREN";
        case TokenType::RPAREN:
            return "RPAREN";
        case TokenType::UNK:
            return "UNK";
        case TokenType::EOT:
            return "EOT";
        default:
            return "UNK";
        }
    }

    std::ostream &operator<<(std::ostream &os, const Token &token)
    {
        os << token.to_string();
        return os;
    }

} // namespace first