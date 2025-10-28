package com.alien_breach.demo.services;

import com.alien_breach.demo.models.GameEvent;
import com.alien_breach.demo.models.GameState;
import com.alien_breach.demo.models.Player;
import com.alien_breach.demo.repositories.GameRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class GameService {

    @Autowired
    private GameRepository gameRepository;

    public GameState startGame(Player player) {
        GameState state = new GameState();
        state.setPlayer(player);
        state.setLives(3);
        state.setScore(0);
        state.setLevel(1);
        state.setScreen("play");
        state.setGameOver(false);
        return gameRepository.save(state);
    }

    public GameState addPoints(Long gameId, int points) {
        GameState state = gameRepository.findById(gameId);
        if (state != null && !state.isGameOver()) {
            state.setScore(state.getScore() + points);
            return gameRepository.save(state);
        }
        return null;
    }

    public GameState updateScreen(Long gameId, String screen) {
        GameState state = gameRepository.findById(gameId);
        if (state != null) {
            state.setScreen(screen);
            return gameRepository.save(state);
        }
        return null;
    }

    public GameState loseLife(Long gameId) {
        GameState state = gameRepository.findById(gameId);
        state.setLives(state.getLives() - 1);
        if (state.getLives() <= 0) state.setGameOver(true);
        return gameRepository.save(state);
    }

    public GameState levelUp(Long gameId) {
        GameState state = gameRepository.findById(gameId);
        state.setLevel(state.getLevel() + 1);
        return gameRepository.save(state);
    }

    public GameState gameOver(Long gameId) {
        GameState state = gameRepository.findById(gameId);
        state.setGameOver(true);
        return gameRepository.save(state);
    }

}
